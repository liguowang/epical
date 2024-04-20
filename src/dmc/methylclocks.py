#!/usr/bin/env python3

"""
Description
-----------
This program computes the biological age using DNA methylation data.
"""

import sys
import os
import pandas as pd
import numpy as np
import importlib.resources
import pickle
import logging
from dmc.utils import plot_coef, plot_corr
from dmc.imputation import impute_beta
from dmc.utils import plot_known_predicted_ages
from dmc.utils import pearson_correlation
import subprocess
from EpigeneticPacemaker.EpigeneticPacemaker import EpigeneticPacemaker
from EpigeneticPacemaker.EpigeneticPacemakerCV import EpigeneticPacemakerCV


__author__ = "Liguo Wang"
__copyright__ = "Copyleft"
__credits__ = []
__maintainer__ = "Liguo Wang"
__email__ = "wang.liguo@mayo.edu"
__status__ = "Development"


def clock_blup_en(beta_file, outfile, metafile=None, delimiter=None,
                  cname="Zhang_BLUP", ff='pdf', na_percent=0.2,
                  ovr=False, imputation_method=6, ext_file=None):
    """
    Calculate DNAm age using the "Zhang_BLUP" or "Zhang_EN" clocks.

    Parameters
    ----------
    beta_file : str
        The input tabular structure file containing DNA methylation data.

        #example of CSV file
        ID_REF,s55N,s58N,s64N,s68N,s72N,s74N,s76N,s77N
        cg26928153,0.86,0.79695,0.72618,0.67142,0.70801,0.80371,0.87158,0.78885
        cg16269199,0.74,0.64148,0.65569,0.64138,0.56486,0.5707,0.75318,0.67239
        cg13869341,0.76,0.7559,0.7059,0.82141,0.72888,0.72055,0.87058,0.80822
        ...
    outfile : str
        The prefix of out files.
    metafile : str, optional
        Meta information (e.g., Age, Sex) of samples.
        Example of a meta file
            Sample_ID       Age     Sex
            s16N    65      M
            s36N    60      F
            s45N    61      M
            ...
    delimiter : str, optional
        Character used to separate columns of the input file.
        The default is None
    cname : str, optional
        Clock name. Must be one of ["Zhang_BLUP", "Zhang_EN"].
        The default is "Zhang_BLUP".
        The default is "Horvath_2013".
    ff : str, optional
        The figure format. Must be one of ['pdf', 'png'].
        The default is 'pdf'.
    na_percent : float, optional
        The maximum of percent of missing values.
        The default is 0.2 (20%).
    ovr : bool, optional
        If set, over write existing files. The default is False
    imputation_method : int
        Must be one of [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. See
        imputation.py for details. default is 6.
    ext_file : str
        This is must be exisit if imputation_method is set to 10.
        Two-column, Tab or comma separated file: 1st column is CpG ID, the 2nd
        column is beta value.

    Returns
    -------
    Pandas Series.
    """

    # set up the prefix for output files.
    if outfile is not None:
        out_prefix = outfile
    else:
        out_prefix = cname + '_out'
    logging.info(
        "The prefix of output files is set to \"%s\"." % out_prefix)

    used_cpg_out = out_prefix + '.predictorCpG_found.tsv'
    missed_cpg_out = out_prefix + '.predictorCpG_missed.tsv'
    age_out = out_prefix + '.DNAm_age.tsv'
    coef_out = out_prefix + '.predictorCpG_coef.tsv'
    r_out = out_prefix + '.plots.R'
    if ff.lower() in ['pdf', 'png']:
        figure_out = out_prefix + '.coef_plot.' + ff.lower()
        scatter_out = out_prefix + '.scatter_plot.' + ff.lower()
    else:
        logging.error("Does not suppor format: %s!" % ff)
        sys.exit(0)
    outfiles = [used_cpg_out, missed_cpg_out, age_out, coef_out, r_out,
                figure_out, scatter_out]

    if ovr is True:
        logging.warning(
            "Over write existing files with prefix: %s" % out_prefix)
        for tmp in outfiles:
            try:
                os.remove(tmp)
            except FileNotFoundError:
                pass
    else:
        for tmp in outfiles:
            if os.path.exists(tmp):
                logging.error(
                    "%s exists! Use different prefix or specify \
                    \"--overwrite\" to replace existing files." % tmp)
                sys.exit(0)

    logging.info("Loading %s clock data ..." % cname)
    if cname == 'Zhang_BLUP':
        fh = importlib.resources.open_binary('dmc.data', 'Zhang_BLUP.pkl')
    elif cname == 'Zhang_EN':
        fh = importlib.resources.open_binary('dmc.data', 'Zhang_EN.pkl')
    clock_dat = pickle.load(fh)

    logging.info("Clock's name: \"%s\"" % clock_dat.name)
    logging.info(
        "Clock was trained from: \"%s\"" %
        ','.join(clock_dat.tissues))
    logging.info("Clock's unit: \"%s\"" % clock_dat.unit)
    logging.info("Number of CpGs used: %d" % clock_dat.ncpg)
    logging.info("Clock's description: \"%s\"" % clock_dat.info)
    clock_coef = pd.Series(clock_dat.coef, name='Coef')
    clock_intercept = clock_dat.Intercept

    logging.info("Read input file: \"%s\"" % beta_file)
    input_df1 = pd.read_csv(beta_file, sep=None, index_col=0, engine='python')

    input_df2 = impute_beta(input_df1, method=imputation_method, ref=ext_file)

    (n_cpg, n_sample) = input_df2.shape
    logging.info(
        "Input file: \"%s\", Number of CpGs: %d, Number of samples: %d" %
        (beta_file, n_cpg, n_sample))
    sample_cpg_ids = input_df2.index
    # sample_names = df2.columns

    logging.info("Standardization ...")
    scaled_df2 = (input_df2 - input_df2.mean())/input_df2.std()

    logging.info("Extract clock CpGs ...")
    # clock CpGs missed from data file
    missed_cpgs = set(clock_coef.index) - set(sample_cpg_ids)
    logging.info(
        "Clock CpGs missed from '%s': %d (%f%%)" %
        (beta_file, len(missed_cpgs), len(missed_cpgs)*100/clock_dat.ncpg))

    if len(missed_cpgs)/clock_dat.ncpg > na_percent:
        logging.critical(
            "Missing clock CpGs exceed %f%%. Exit!" % (na_percent*100))
        sys.exit(0)

    common_cpgs = list(set(clock_coef.index) & set(sample_cpg_ids))
    logging.info(
        "Clock CpGs exisit in \"%s\": %d" % (beta_file, len(common_cpgs)))

    used_df = scaled_df2.loc[common_cpgs]
    used_clock_coef = clock_coef.loc[common_cpgs]
    (usable_cpg, usable_sample) = used_df.shape
    logging.info(
        "Used CpGs: %d, Used samples: %d" % (usable_cpg, usable_sample))

    df4 = used_df.mul(used_clock_coef, axis=0)

    output = df4.sum(axis=0) + clock_intercept
    output.name = "%s" % cname

    if metafile is not None:
        logging.info("Read meta information file: \"%s\"" % metafile)
        meta_df = pd.read_csv(metafile, sep=None, index_col=0, engine='python')
        meta_df.index = meta_df.index.astype(str)
        # combine predicted age and other meta information
        logging.info("Combining meta information with predicted age")
        output = pd.concat([output, meta_df], axis=1)

        # generate scatter plot between c_age and d_age
        c_age = []
        for col_id in output.columns:
            if col_id.lower() == 'age':
                c_age = output[col_id]
                break
        d_age = output[cname]

        if len(c_age) >= 2 and len(c_age) == len(d_age):
            logging.info(
                "Writing R script of scatter plot. Save to: %s" % r_out)
            plot_corr(c_age, d_age, outfile=scatter_out, rfile=r_out)

    # save used CpGs to file
    logging.info("Save used CpGs and beta values to: %s" % used_cpg_out)
    used_df.to_csv(used_cpg_out, sep="\t", index_label="CpG_ID")

    # save missed CpGs to file
    logging.info("Save missed CpGs: %s" % missed_cpg_out)
    tmp = pd.DataFrame(list(missed_cpgs), columns=["missed_CpGs"])
    tmp.to_csv(missed_cpg_out, sep="\t", index=False)

    # save coef information
    logging.info("Save CpG and coefficients to: %s" % coef_out)
    tmp = clock_coef.to_frame()
    tmp['Found'] = tmp.index.isin(common_cpgs)
    tmp.to_csv(coef_out, sep="\t", index_label="CpG_ID")

    # save predicted age
    logging.info("Save predicted DNAm age to: %s" % age_out)
    output.to_csv(age_out, sep="\t", index_label="Sample_ID")

    # generate coefficient plot
    logging.info("Writing R script of coefficient plot. Save to: %s" % r_out)
    plot_coef(coef_out, figure_out, r_out)

    logging.info("Running R script: %s" % r_out)
    try:
        subprocess.call("Rscript " + r_out, shell=True)
    except subprocess.CalledProcessError as e:
        print("Cannot generate pdf file from " + r_out, file=sys.stderr)
        print(e.output, file=sys.stderr)
        pass
    return output


def clock_horvath(beta_file, outfile, metafile=None, delimiter=None, adult_age=20,
                  cname="Horvath_2013", ff='pdf', na_percent=0.2, ovr=False,
                  imputation_method=6, ext_file=None):
    """
    Calculate DNAm age using the "Horvath_2013", "Horvath_2018", "PedPE" or
    "Ped_Wu" clocks.

    Parameters
    ----------
    beta_file : str
        The input tabular structure file containing DNA methylation data.
        #example of CSV file
        ID_REF,s55N,s58N,s64N,s68N,s72N,s74N,s76N,s77N
        cg26928153,0.86007,0.79695,0.72618,0.67142,0.70801,0.80371,0.87158,0.78885
        cg16269199,0.74023,0.64148,0.65569,0.64138,0.56486,0.5707,0.75318,0.67239
        cg13869341,0.76405,0.7559,0.7059,0.82141,0.72888,0.72055,0.87058,0.80822
        ...
    outfile : str
        The prefix of out files.
    metafile : str, optional
        Meta information (e.g., Age, Sex) of samples.
        Example of a meta file
            Sample_ID       Age     Sex
            s16N    65      M
            s36N    60      F
            s45N    61      M
            ...
    delimiter : str, optional
        Character used to separate columns of the input file.
        The default is None
    adult_age : int, optional
        Default is 20. Do not change this value.
    cname : str, optional
        Clock name. Must be one of ["Horvath_2013", "Horvath_2018", "PedPE",
        "Ped_Wu", "MEAT"]. The default is "Horvath_2013".
    ff : str, optional
        The figure format. Must be one of ['pdf', 'png'].
        The default is 'pdf'.
    na_percent : float, optional
        The maximum of percent of missing values.
        The default is 0.2 (20%).
    ovr : bool, optional
        If set, over write existing files. The default is False
    imputation_method : int
        Must be one of [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. See
        imputation.py for details. default is 6.
    ext_file : str
        This is must be exisit if imputation_method is set to 10.
        Two-column, Tab or comma separated file: 1st column is CpG ID, the 2nd
        column is beta value.

    Returns
    -------
    Pandas Series.

    """
    # set up the prefix for output files.
    if outfile is not None:
        out_prefix = outfile
    else:
        out_prefix = cname + '_out'
    logging.info(
        "The prefix of output files is set to \"%s\"." % out_prefix)

    used_cpg_out = out_prefix + '.predictorCpG_found.tsv'
    missed_cpg_out = out_prefix + '.predictorCpG_missed.tsv'
    age_out = out_prefix + '.DNAm_age.tsv'
    coef_out = out_prefix + '.predictorCpG_coef.tsv'
    r_out = out_prefix + '.plots.R'
    if ff.lower() in ['pdf', 'png']:
        figure_out = out_prefix + '.coef_plot.' + ff.lower()
        scatter_out = out_prefix + '.scatter_plot.' + ff.lower()
    else:
        logging.error("Does not suppor format: %s!" % ff)
        sys.exit(0)
    outfiles = [used_cpg_out, missed_cpg_out, age_out, coef_out, r_out,
                figure_out, scatter_out]

    if ovr is True:
        logging.warning(
            "Over write existing files with prefix: %s" % out_prefix)
        for tmp in outfiles:
            try:
                os.remove(tmp)
            except FileNotFoundError:
                pass
    else:
        for tmp in outfiles:
            if os.path.exists(tmp):
                logging.error(
                    "%s exists! Use different prefix or specify \
                    \"--overwrite\" to replace existing files." % tmp)
                sys.exit(0)

    logging.info("Loading %s clock data ..." % cname)
    if cname.lower() == 'Horvath13'.lower():
        fh = importlib.resources.open_binary('dmc.data', 'Horvath13.pkl')
    if cname.lower() == 'Horvath13_shrunk'.lower():
        fh = importlib.resources.open_binary('dmc.data', 'Horvath13_shrunk.pkl')
    elif cname.lower() == 'Horvath18'.lower():
        fh = importlib.resources.open_binary('dmc.data', 'Horvath18.pkl')
    elif cname.lower() == 'PedBE'.lower():
        fh = importlib.resources.open_binary('dmc.data', 'Ped_McEwen.pkl')
    elif cname == 'Ped_Wu':
        fh = importlib.resources.open_binary('dmc.data', 'Ped_Wu.pkl')
    elif cname == 'Cortical':
        fh = importlib.resources.open_binary('dmc.data', 'CorticalClock.pkl')
    elif cname == 'MEAT':
        fh = importlib.resources.open_binary('dmc.data', 'MEAT.pkl')
    clock_dat = pickle.load(fh)

    logging.info("Clock's name: \"%s\"" % clock_dat.name)
    logging.info(
        "Clock was trained from: \"%s\"" % ','.join(clock_dat.tissues))
    logging.info("Clock's unit: \"%s\"" % clock_dat.unit)
    logging.info("Number of CpGs used: %d" % clock_dat.ncpg)
    logging.info("Clock's description: \"%s\"" % clock_dat.info)
    clock_coef = pd.Series(clock_dat.coef, name='Coef')
    clock_intercept = clock_dat.Intercept

    logging.info("Read input file: \"%s\"" % beta_file)
    input_df1 = pd.read_csv(
        beta_file, sep=delimiter, index_col=0, engine='python')

    input_df2 = impute_beta(input_df1, method=imputation_method, ref=ext_file)
    (n_cpg, n_sample) = input_df2.shape
    logging.info(
        "Input file: \"%s\", Number of CpGs: %d, Number of samples: %d" %
        (beta_file, n_cpg, n_sample))
    sample_cpg_ids = input_df2.index
    # sample_names = df2.columns

    # printlog("Standardization ...")
    # scaled_df2 = (input_df2 - input_df2.mean())/input_df2.std()

    logging.info("Extract clock CpGs ...")
    # clock CpGs missed from data file
    missed_cpgs = set(clock_coef.index) - set(sample_cpg_ids)
    logging.info(
        "Clock CpGs missed from '%s': %d (%f%%)" %
        (beta_file, len(missed_cpgs), len(missed_cpgs)*100/clock_dat.ncpg))

    if len(missed_cpgs)/clock_dat.ncpg > na_percent:
        logging.critical(
            "Missing clock CpGs exceed %f%%. Exit!" % (na_percent*100))
        sys.exit(0)

    common_cpgs = list(set(clock_coef.index) & set(sample_cpg_ids))
    logging.info(
        "Clock CpGs exisit in \"%s\": %d" % (beta_file, len(common_cpgs)))

    used_df = input_df2.loc[common_cpgs]
    used_clock_coef = clock_coef.loc[common_cpgs]
    (usable_cpg, usable_sample) = used_df.shape
    logging.info(
        "Used CpGs: %d, Used samples: %d" % (usable_cpg, usable_sample))

    df4 = used_df.mul(used_clock_coef, axis=0)

    # df4.to_csv('df4.csv')
    output = df4.sum(axis=0) + clock_intercept
    # adoped from the "anti.trafo" funciton from:
    # https://rdrr.io/github/perishky/meffonym/src/tests/horvath-example.r
    for indx, val in output.items():
        if val < 0:
            if cname == 'Ped_Wu':
                output[indx] = ((1 + adult_age)*np.exp(val) - 1)/12.0
            else:
                output[indx] = (1 + adult_age)*np.exp(val) - 1
        else:
            if cname == 'Ped_Wu':
                output[indx] = ((1 + adult_age)*val + adult_age)/12.0
            else:
                output[indx] = (1 + adult_age)*val + adult_age
    output.name = "%s" % cname

    if metafile is not None:
        logging.info("Read meta information file: \"%s\"" % metafile)
        meta_df = pd.read_csv(metafile, sep=None, index_col=0, engine='python')
        meta_df.index = meta_df.index.astype(str)
        # combine predicted age and other meta information
        logging.info("Combining meta information with predicted age")
        output = pd.concat([output, meta_df], axis=1)

        # generate scatter plot between c_age and d_age
        c_age = []
        for col_id in output.columns:
            if col_id.lower() == 'age':
                c_age = output[col_id]
                break
        d_age = output[cname]

        if len(c_age) >= 2 and len(c_age) == len(d_age):
            logging.info(
                "Writing R script of scatter plot. Save to: %s" % r_out)
            plot_corr(c_age, d_age, outfile=scatter_out, rfile=r_out)

    # save used CpGs to file
    logging.info("Save used CpGs and beta values to: %s" % used_cpg_out)
    used_df.to_csv(used_cpg_out, sep="\t", index_label="CpG_ID")

    # save missed CpGs to file
    logging.info("Save missed CpGs: %s" % missed_cpg_out)
    tmp = pd.DataFrame(list(missed_cpgs), columns=["missed_CpGs"])
    tmp.to_csv(missed_cpg_out, sep="\t", index=False)

    # save coef information
    logging.info("Save CpG and coefficients to: %s" % coef_out)
    tmp = clock_coef.to_frame()
    tmp['Found'] = tmp.index.isin(common_cpgs)
    tmp.to_csv(coef_out, sep="\t", index_label="CpG_ID")

    # save predicted age
    logging.info("Save predicted DNAm age to: %s" % age_out)
    output.to_csv(age_out, sep="\t", index_label="Sample_ID")

    # generate coefficient plot
    logging.info("Generate coefficient plot. Save to: %s" % figure_out)
    plot_coef(coef_out, figure_out, r_out)

    logging.info("Running R script: %s" % r_out)
    try:
        subprocess.call("Rscript " + r_out, shell=True)
    except subprocess.CalledProcessError as e:
        print("Cannot generate pdf file from " + r_out, file=sys.stderr)
        print(e.output, file=sys.stderr)
        pass

    return output


def clock_levine_hannum(beta_file, outfile, metafile=None, delimiter=None,
                        cname="Levine", ff='pdf', na_percent=0.2, ovr=False,
                        imputation_method=6, ext_file=None):
    """
    Calculate DNAm age using the "Levine", "Hannum", or "Lu_DNAmTL" clock.
    Note, the output of "Lu_DNAmTL" clock is "Kb" (DNA telomere length)

    Parameters
    ----------
    beta_file : str
        The input tabular structure file containing DNA methylation data.
        #example of CSV file
        ID_REF,s55N,s58N,s64N,s68N,s72N,s74N,s76N,s77N
        cg26928153,0.86007,0.79695,0.72618,0.67142,0.70801,0.80371,0.8715,0.789
        cg16269199,0.74023,0.64148,0.65569,0.64138,0.56486,0.5707,0.7531,0.672
        cg13869341,0.76405,0.7559,0.7059,0.82141,0.72888,0.72055,0.8705,0.808
        ...
    outfile : str
        The prefix of out files.
    metafile : str, optional
        Meta information (e.g., Age, Sex) of samples.
        Example of a meta file
            Sample_ID       Age     Sex
            s16N    65      M
            s36N    60      F
            s45N    61      M
            ...
    delimiter : str, optional
        Character used to separate columns of the input file.
        The default is None
    cname : str, optional
        Clock name. Must be one of ["Levine", "Hannum", "Lu_DNAmTL"].
        The default is "Levine".
    ff : str, optional
        The figure format. Must be one of ['pdf', 'png'].
        The default is 'pdf'.
    na_percent : float, optional
        The maximum of percent of missing values.
        The default is 0.2 (20%).
    ovr : bool, optional
        If set, over write existing files. The default is False
    imputation_method : int
        Must be one of [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. See
        imputation.py for details. default is 6.
    ext_file : str
        This is must be exisit if imputation_method is set to 10.
        Two-column, Tab or comma separated file: 1st column is CpG ID, the 2nd
        column is beta value.

    Returns
    -------
    Pandas Series.
    """

    # set up the prefix for output files.
    if outfile is not None:
        out_prefix = outfile
    else:
        out_prefix = cname + '_out'
    logging.info(
        "The prefix of output files is set to \"%s\"." % out_prefix)

    used_cpg_out = out_prefix + '.predictorCpG_found.tsv'
    missed_cpg_out = out_prefix + '.predictorCpG_missed.tsv'
    age_out = out_prefix + '.DNAm_age.tsv'
    coef_out = out_prefix + '.predictorCpG_coef.tsv'
    r_out = out_prefix + '.plots.R'
    if ff.lower() in ['pdf', 'png']:
        figure_out = out_prefix + '.coef_plot.' + ff.lower()
        scatter_out = out_prefix + '.scatter_plot.' + ff.lower()
    else:
        logging.error("Does not suppor format: %s!" % ff)
        sys.exit(0)
    outfiles = [used_cpg_out, missed_cpg_out, age_out, coef_out, r_out,
                figure_out, scatter_out]

    if ovr is True:
        logging.warning(
            "Over write existing files with prefix: %s" % out_prefix)
        for tmp in outfiles:
            try:
                os.remove(tmp)
            except FileNotFoundError:
                continue
    else:
        for tmp in outfiles:
            if os.path.exists(tmp):
                logging.error(
                    "%s exists! Use different prefix or specify \
                    \"--overwrite\" to replace existing files." % tmp)
                sys.exit(0)

    logging.info("Loading %s clock data ..." % cname)
    if cname.lower() == 'Levine'.lower():
        fh = importlib.resources.open_binary('dmc.data', 'Levine.pkl')
    elif cname.lower() == 'Hannum'.lower():
        fh = importlib.resources.open_binary('dmc.data', 'Hannum.pkl')
    elif cname.lower() == 'Lu_DNAmTL'.lower():
        fh = importlib.resources.open_binary('dmc.data', 'Lu_DNAmTL.pkl')
    clock_dat = pickle.load(fh)

    logging.info("Clock's name: \"%s\"" % clock_dat.name)
    logging.info(
        "Clock was trained from: \"%s\"" % ','.join(clock_dat.tissues))
    logging.info("Clock's unit: \"%s\"" % clock_dat.unit)
    logging.info("Number of CpGs used: %d" % clock_dat.ncpg)
    logging.info("Clock's description: \"%s\"" % clock_dat.info)
    clock_coef = pd.Series(clock_dat.coef, name='Coef')
    clock_intercept = clock_dat.Intercept

    logging.info("Read input file: \"%s\"" % beta_file)
    input_df1 = pd.read_csv(beta_file, sep=None, index_col=0, engine='python')

    input_df2 = impute_beta(input_df1, method=imputation_method, ref=ext_file)
    (n_cpg, n_sample) = input_df2.shape
    logging.info(
        "Input file: \"%s\", Number of CpGs: %d, Number of samples: %d" %
        (beta_file, n_cpg, n_sample))
    sample_cpg_ids = input_df2.index
    # sample_names = df2.columns

    # printlog("Standardization ...")
    # scaled_df2 = (input_df2 - input_df2.mean())/input_df2.std()

    logging.info("Extract clock CpGs ...")
    # clock CpGs missed from data file
    missed_cpgs = set(clock_coef.index) - set(sample_cpg_ids)
    logging.info(
        "Clock CpGs missed from '%s': %d (%f%%)" %
        (beta_file, len(missed_cpgs), len(missed_cpgs)*100/clock_dat.ncpg))

    if len(missed_cpgs)/clock_dat.ncpg > na_percent:
        logging.critical(
            "Missing clock CpGs exceed %f%%. Exit!" % (na_percent*100))
        sys.exit(0)

    common_cpgs = list(set(clock_coef.index) & set(sample_cpg_ids))
    logging.info(
        "Clock CpGs exisit in \"%s\": %d" % (beta_file, len(common_cpgs)))

    used_df = input_df2.loc[common_cpgs]
    used_clock_coef = clock_coef.loc[common_cpgs]
    (usable_cpg, usable_sample) = used_df.shape
    logging.info(
        "Used CpGs: %d, Used samples: %d" % (usable_cpg, usable_sample))

    df4 = used_df.mul(used_clock_coef, axis=0)

    # df4.to_csv('df4.csv')
    output = df4.sum(axis=0) + clock_intercept

    output.name = "%s" % cname

    if metafile is not None:
        logging.info("Read meta information file: \"%s\"" % metafile)
        meta_df = pd.read_csv(metafile, sep=None, index_col=0, engine='python')
        meta_df.index = meta_df.index.astype(str)
        # combine predicted age and other meta information
        logging.info("Combining meta information with predicted age")
        output = pd.concat([output, meta_df], axis=1)

        # generate scatter plot between c_age and d_age
        c_age = []
        for col_id in output.columns:
            if col_id.lower() == 'age':
                c_age = output[col_id]
                break
        d_age = output[cname]

        if len(c_age) >= 2 and len(c_age) == len(d_age):
            logging.info(
                "Writing R script of scatter plot. Save to: %s" % r_out)
            plot_corr(c_age, d_age, outfile=scatter_out, rfile=r_out)

    # save used CpGs to file
    logging.info("Save used CpGs and beta values to: %s" % used_cpg_out)
    used_df.to_csv(used_cpg_out, sep="\t", index_label="CpG_ID")

    # save missed CpGs to file
    logging.info("Save missed CpGs: %s" % missed_cpg_out)
    tmp = pd.DataFrame(list(missed_cpgs), columns=["missed_CpGs"])
    tmp.to_csv(missed_cpg_out, sep="\t", index=False)

    # save coef information
    logging.info("Save CpG and coefficients to: %s" % coef_out)
    tmp = clock_coef.to_frame()
    tmp['Found'] = tmp.index.isin(common_cpgs)
    tmp.to_csv(coef_out, sep="\t", index_label="CpG_ID")

    # save predicted age
    logging.info("Save predicted DNAm age to: %s" % age_out)
    output.to_csv(age_out, sep="\t", index_label="Sample_ID")

    # generate coefficient plot
    logging.info("Generate coefficient plot. Save to: %s" % figure_out)
    plot_coef(coef_out, figure_out, r_out)

    logging.info("Running R script: %s" % r_out)
    try:
        subprocess.call("Rscript " + r_out, shell=True)
    except subprocess.CalledProcessError as e:
        print("Cannot generate pdf file from " + r_out, file=sys.stderr)
        print(e.output, file=sys.stderr)
        pass
    return output


def clock_GA(beta_file, outfile, metafile=None, delimiter=None,
             cname="GA_Knight", ff='pdf', na_percent=0.2, ovr=False,
             imputation_method=6, ext_file=None):
    """
    Calculate DNAm age (gestational) using the 'Knight', 'Bohlin', 'Mayne',
    'Haftorn', 'Lee_CPC', 'Lee_RPC', or 'Lee_cRPC' clock.

    Parameters
    ----------
    beta_file : str
        The input tabular structure file containing DNA methylation data.
        #example of CSV file
        ID_REF,s55N,s58N,s64N,s68N,s72N,s74N,s76N,s77N
        cg26928153,0.86007,0.79695,0.72618,0.67142,0.70801,0.80371,0.87158,0.78885
        cg16269199,0.74023,0.64148,0.65569,0.64138,0.56486,0.5707,0.75318,0.67239
        cg13869341,0.76405,0.7559,0.7059,0.82141,0.72888,0.72055,0.87058,0.80822
        ...
    outfile : str
        The prefix of out files.
    metafile : str, optional
        Meta information (e.g., Age, Sex) of samples.
        Example of a meta file
            Sample_ID       Age     Sex
            s16N    65      M
            s36N    60      F
            s45N    61      M
            ...
    delimiter : str, optional
        Character used to separate columns of the input file.
        The default is None
    cname : str, optional
        Clock name. Must be one of ['GA_Knight', 'GA_Bohlin', 'GA_Mayne',
        'GA_Haftorn', 'GA_Lee_CPC', 'GA_Lee_RPC', 'GA_Lee_rRPC'].
        The default is "GA_Knight".
    ff : str, optional
        The figure format. Must be one of ['pdf', 'png'].
        The default is 'pdf'.
    na_percent : float, optional
        The maximum of percent of missing values.
        The default is 0.2 (20%).
    ovr : bool, optional
        If set, over write existing files. The default is False
    imputation_method : int
        Must be one of [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. See
        imputation.py for details. default is 6.
    ext_file : str
        This is must be exisit if imputation_method is set to 10.
        Two-column, Tab or comma separated file: 1st column is CpG ID, the 2nd
        column is beta value.

    Returns
    -------
    Pandas Series.
    """
    # set up the prefix for output files.
    if outfile is not None:
        out_prefix = outfile
    else:
        out_prefix = cname + '_out'
    logging.info(
        "The prefix of output files is set to \"%s\"." % out_prefix)

    used_cpg_out = out_prefix + '.predictorCpG_found.tsv'
    missed_cpg_out = out_prefix + '.predictorCpG_missed.tsv'
    age_out = out_prefix + '.DNAm_age.tsv'
    coef_out = out_prefix + '.predictorCpG_coef.tsv'
    r_out = out_prefix + '.plots.R'
    if ff.lower() in ['pdf', 'png']:
        figure_out = out_prefix + '.coef_plot.' + ff.lower()
        scatter_out = out_prefix + '.scatter_plot.' + ff.lower()
    else:
        logging.error("Does not suppor format: %s!" % ff)
        sys.exit(0)
    outfiles = [used_cpg_out, missed_cpg_out, age_out, coef_out, r_out,
                figure_out, scatter_out]

    if ovr is True:
        logging.warning(
            "Over write existing files with prefix: %s" % out_prefix)
        for tmp in outfiles:
            try:
                os.remove(tmp)
            except FileNotFoundError:
                pass
    else:
        for tmp in outfiles:
            if os.path.exists(tmp):
                logging.error("%s exists! Use different prefix or specify \
                             \"--overwrite\" to replace existing files." % tmp)
                sys.exit(0)

    logging.info("Loading %s clock data ..." % cname)
    if cname == 'GA_Knight':
        fh = importlib.resources.open_binary('dmc.data', 'GA_Knight.pkl')
    elif cname == 'GA_Bohlin':
        fh = importlib.resources.open_binary('dmc.data', 'GA_Bohlin.pkl')
    elif cname == 'GA_Mayne':
        fh = importlib.resources.open_binary('dmc.data', 'GA_Mayne.pkl')
    elif cname == 'GA_Haftorn':
        fh = importlib.resources.open_binary('dmc.data', 'GA_Haftorn.pkl')
    elif cname == 'GA_Lee_CPC':
        fh = importlib.resources.open_binary('dmc.data', 'GA_Lee_CPC.pkl')
    elif cname == 'GA_Lee_RPC':
        fh = importlib.resources.open_binary('dmc.data', 'GA_Lee_RPC.pkl')
    elif cname == 'GA_Lee_rRPC':
        fh = importlib.resources.open_binary(
            'dmc.data', 'GA_Lee_refined_RPC.pkl')
    clock_dat = pickle.load(fh)

    logging.info("Clock's name: \"%s\"" % clock_dat.name)
    logging.info(
        "Clock was trained from: \"%s\"" % ','.join(clock_dat.tissues))
    logging.info("Clock's unit: \"%s\"" % clock_dat.unit)
    logging.info("Number of CpGs used: %d" % clock_dat.ncpg)
    logging.info("Clock's description: \"%s\"" % clock_dat.info)
    clock_coef = pd.Series(clock_dat.coef, name='Coef')
    clock_intercept = clock_dat.Intercept

    logging.info("Read input file: \"%s\"" % beta_file)
    input_df1 = pd.read_csv(beta_file, sep=None, index_col=0, engine='python')

    input_df2 = impute_beta(input_df1, method=imputation_method, ref=ext_file)
    (n_cpg, n_sample) = input_df2.shape
    logging.info(
        "Input file: \"%s\", Number of CpGs: %d, Number of samples: %d" %
        (beta_file, n_cpg, n_sample))
    sample_cpg_ids = input_df2.index
    # sample_names = df2.columns

    # printlog("Standardization ...")
    # scaled_df2 = (input_df2 - input_df2.mean())/input_df2.std()

    logging.info("Extract clock CpGs ...")
    # clock CpGs missed from data file
    missed_cpgs = set(clock_coef.index) - set(sample_cpg_ids)
    logging.info(
        "Clock CpGs missed from '%s': %d (%f%%)" %
        (beta_file, len(missed_cpgs), len(missed_cpgs)*100/clock_dat.ncpg))

    if len(missed_cpgs)/clock_dat.ncpg > na_percent:
        logging.critical(
            "Missing clock CpGs exceed %f%%. Exit!" % (na_percent*100))
        sys.exit(0)

    common_cpgs = list(set(clock_coef.index) & set(sample_cpg_ids))
    logging.info(
        "Clock CpGs exisit in \"%s\": %d" % (beta_file, len(common_cpgs)))

    used_df = input_df2.loc[common_cpgs]
    used_clock_coef = clock_coef.loc[common_cpgs]
    (usable_cpg, usable_sample) = used_df.shape
    logging.info(
        "Used CpGs: %d, Used samples: %d" % (usable_cpg, usable_sample))

    df4 = used_df.mul(used_clock_coef, axis=0)

    # df4.to_csv('df4.csv')
    output = df4.sum(axis=0) + clock_intercept
    output.name = "%s" % cname
    if metafile is not None:
        logging.info("Read meta information file: \"%s\"" % metafile)
        meta_df = pd.read_csv(metafile, sep=None, index_col=0, engine='python')
        meta_df.index = meta_df.index.astype(str)
        # combine predicted age and other meta information
        logging.info("Combining meta information with predicted age")
        output = pd.concat([output, meta_df], axis=1)
        # print(output.to_string())
        # generate scatter plot between c_age and d_age
        c_age = []
        for col_id in output.columns:
            if col_id.lower() == 'age':
                c_age = output[col_id]
                break
        d_age = output[cname]
        if len(c_age) >= 2 and len(c_age) == len(d_age):
            logging.info(
                "Writing R script of scatter plot. Save to: %s" % r_out)
            plot_corr(c_age, d_age, outfile=scatter_out, rfile=r_out)

    # save used CpGs to file
    logging.info("Save used CpGs and beta values to: %s" % used_cpg_out)
    used_df.to_csv(used_cpg_out, sep="\t", index_label="CpG_ID")

    # save missed CpGs to file
    logging.info("Save missed CpGs: %s" % missed_cpg_out)
    tmp = pd.DataFrame(list(missed_cpgs), columns=["missed_CpGs"])
    tmp.to_csv(missed_cpg_out, sep="\t", index=False)

    # save coef information
    logging.info("Save CpG and coefficients to: %s" % coef_out)
    tmp = clock_coef.to_frame()
    tmp['Found'] = tmp.index.isin(common_cpgs)
    tmp.to_csv(coef_out, sep="\t", index_label="CpG_ID")

    # save predicted age
    logging.info("Save predicted DNAm age to: %s" % age_out)
    output.to_csv(age_out, sep="\t", index_label="Sample_ID")

    # generate coefficient plot
    logging.info("Generate coefficient plot. Save to: %s" % figure_out)
    plot_coef(coef_out, figure_out, r_out)

    logging.info("Running R script: %s" % r_out)
    try:
        subprocess.call("Rscript " + r_out, shell=True)
    except subprocess.CalledProcessError as e:
        print("Cannot generate pdf file from " + r_out, file=sys.stderr)
        print(e.output, file=sys.stderr)
        pass
    return output


def altum_age(beta_file, outfile, metafile=None, delimiter=None,
              cname="AltumAge", ff='pdf', na_percent=0.2, ovr=False,
              imputation_method=6, ext_file=None):
    """
    Calculate DNAm age (gestational) using the 'Knight', 'Bohlin', 'Mayne',
    'Haftorn', or 'Lee' clock.

    Parameters
    ----------
    beta_file : str
        The input tabular structure file containing DNA methylation data.
        #example of CSV file
        ID_REF,s55N,s58N,s64N,s68N,s72N,s74N,s76N,s77N
        cg26928153,0.86007,0.79695,0.72618,0.67142,0.70801,0.80371,0.87158,0.78885
        cg16269199,0.74023,0.64148,0.65569,0.64138,0.56486,0.5707,0.75318,0.67239
        cg13869341,0.76405,0.7559,0.7059,0.82141,0.72888,0.72055,0.87058,0.80822
        ...
    outfile : str
        The prefix of out files.
    metafile : str, optional
        Meta information (e.g., Age, Sex) of samples.
        Example of a meta file
            Sample_ID       Age     Sex
            s16N    65      M
            s36N    60      F
            s45N    61      M
            ...
    delimiter : str, optional
        Character used to separate columns of the input file.
        The default is None
    cname : str, optional
        Clock name. Set to "AltumAge" (do NOT change)
    ff : str, optional
        The figure format. Must be one of ['pdf', 'png'].
        The default is 'pdf'.
    na_percent : float, optional
        The maximum of percent of missing values.
        The default is 0.2 (20%).
    ovr : bool, optional
        If set, over write existing files. The default is False
    imputation_method : int
        Must be one of [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. See
        imputation.py for details. default is 6.
    ext_file : str
        This is must be exisit if imputation_method is set to 10.
        Two-column, Tab or comma separated file: 1st column is CpG ID, the 2nd
        column is beta value.

    Returns
    -------
    Pandas Series.
    """
    import tensorflow as tf
    # from sklearn import linear_model, preprocessing

    # set up the prefix for output files.
    if outfile is not None:
        out_prefix = outfile
    else:
        out_prefix = cname + '_out'
    logging.info(
        "The prefix of output files is set to \"%s\"." % out_prefix)

    used_cpg_out = out_prefix + '.predictorCpG_found.tsv'
    missed_cpg_out = out_prefix + '.predictorCpG_missed.tsv'
    age_out = out_prefix + '.DNAm_age.tsv'
    coef_out = out_prefix + '.predictorCpG_coef.tsv'
    r_out = out_prefix + '.plots.R'
    if ff.lower() in ['pdf', 'png']:
        figure_out = out_prefix + '.coef_plot.' + ff.lower()
        scatter_out = out_prefix + '.scatter_plot.' + ff.lower()
    else:
        logging.error("Does not suppor format: %s!" % ff)
        sys.exit(0)
    outfiles = [used_cpg_out, missed_cpg_out, age_out, coef_out, r_out,
                figure_out, scatter_out]

    if ovr is True:
        logging.warning(
            "Over write existing files with prefix: %s" % out_prefix)
        for tmp in outfiles:
            try:
                os.remove(tmp)
            except FileNotFoundError:
                pass
        for tmp in outfiles:
            if os.path.exists(tmp):
                os.remove(tmp)
    else:
        for tmp in outfiles:
            if os.path.exists(tmp):
                logging.error(
                    "%s exists! Use different prefix or specify \
                    \"--overwrite\" to replace existing files." % tmp)
                sys.exit(0)

    logging.info("Loading %s clock data ..." % cname)
    if cname == 'AltumAge':
        this_dir, this_filename = os.path.split(__file__)
        scaler_path = os.path.join(this_dir, "data", "scaler.pkl")
        model_path = os.path.join(this_dir, "data", "AltumAge.h5")
        cpg_path = os.path.join(this_dir, "data", "multi_platform_cpgs.pkl")

        scaler = pd.read_pickle(scaler_path)
        AltumAge = tf.keras.models.load_model(model_path)
        cpgs = np.array(pd.read_pickle(cpg_path))

        fh = importlib.resources.open_binary('dmc.data', 'AltumAge_cpg.pkl')

    clock_dat = pickle.load(fh)
    logging.info("Clock's name: \"%s\"" % clock_dat.name)
    logging.info(
        "Clock was trained from: \"%s\"" % ','.join(clock_dat.tissues))
    logging.info("Clock's unit: \"%s\"" % clock_dat.unit)
    logging.info("Number of CpGs used: %d" % len(cpgs))
    logging.info("Clock's description: \"%s\"" % clock_dat.info)

    logging.info("Read input file: \"%s\" ..." % beta_file)
    input_df1 = pd.read_csv(beta_file, sep=None, index_col=0, engine='python')

    input_df2 = impute_beta(input_df1, method=imputation_method, ref=ext_file)
    # check if there is any missed CpGs
    missed_cpgs = list(set(cpgs) - set(input_df2.index))
    # print (missed_cpgs)

    logging.info("%d CpGs were missed from %s" % (len(missed_cpgs), beta_file))

    logging.info("Transpose input data frame ...")
    df_transpose = input_df2.T

    if len(missed_cpgs) > 0:
        logging.info("Insert missed CpGs back ...")
        tmp = df_transpose.mean(axis=1)
        for cpg_name in missed_cpgs:
            print(cpg_name)
            df_transpose[cpg_name] = 0

    logging.info("Extract clock CpG from data frame ...")
    df_used = df_transpose[cpgs]

    (usable_sample, usable_cpg) = df_used.shape
    logging.info(
        "Used CpGs: %d, Used samples: %d" % (usable_cpg, usable_sample))

    # AltumAge used the transposed beta value matrix
    logging.info(
        "Scale the beta values of each CpG with sklearn robust scaler ...")
    df_scaled = scaler.transform(df_used)

    logging.info("AltumAge prediction ...")
    pred_age_AltumAge = AltumAge.predict(df_scaled).flatten()
    output = pd.DataFrame(
        index=df_used.index, data={cname: list(pred_age_AltumAge)}
        )
    print(output)
    if metafile is not None:
        logging.info("Read meta information file: \"%s\"" % metafile)
        meta_df = pd.read_csv(metafile, sep=None, index_col=0, engine='python')
        meta_df.index = meta_df.index.astype(str)
        # combine predicted age and other meta information
        logging.info("Combining meta information with predicted age")
        output = pd.concat([output, meta_df], axis=1)

        # generate scatter plot between c_age and d_age
        c_age = []
        for col_id in output.columns:
            if col_id.lower() == 'age':
                c_age = output[col_id]
                break
        d_age = output[cname]

        if len(c_age) >= 2 and len(c_age) == len(d_age):
            logging.info(
                "Writing R script of scatter plot. Save to: %s" % r_out)
            plot_corr(c_age, d_age, outfile=scatter_out, rfile=r_out)

    # save used CpGs to file
    logging.info("Save used CpGs and beta values to: %s" % used_cpg_out)
    df_used.to_csv(used_cpg_out, sep="\t", index_label="CpG_ID")

    # save missed CpGs to file
    # logging.info("Save missed CpGs: %s" % missed_cpg_out)
    # tmp = pd.DataFrame(list(missed_cpgs), columns=["missed_CpGs"])
    # tmp.to_csv(missed_cpg_out, sep="\t", index=False)

    # save predicted age
    logging.info("Save predicted DNAm age to: %s" % age_out)
    output.to_csv(age_out, sep="\t", index_label="Sample_ID")

    logging.info("Running R script: %s" % r_out)
    try:
        subprocess.call("Rscript " + r_out, shell=True)
    except subprocess.CalledProcessError as e:
        print("Cannot generate pdf file from " + r_out, file=sys.stderr)
        print(e.output, file=sys.stderr)
        pass
    return output


def clock_epm(beta_file, metafile, outfile, delimiter=None,
              imputation_method=6, ext_file=None, pcc_cut=0.85,
              iter_n=100, error_tol=1e-5, cv_folds=10, frmt='pdf',
              cname='EPM'):
    """
    Epigenetic Pacemaker (EPM)
    """
    # set up the prefix for output files.
    if outfile is not None:
        out_prefix = outfile
    else:
        out_prefix = cname + '_out'
    logging.info(
        "The prefix of output files is set to \"%s\"." % out_prefix)

    test_age_out = out_prefix + '.test_EPM_age.tsv'
    train_age_out = out_prefix + '.train_EPM_age.tsv'
    test_png_out = out_prefix + '.test_EPM_age.' + frmt
    train_png_out = out_prefix + '.train_EPM_age.' + frmt
    test_cpg_out = out_prefix + '.test_selected_CpGs.tsv'
    train_cpg_out = out_prefix + '.train_selected_CpGs.tsv'

    # Read input beta file
    logging.info("Read input beta file: \"%s\"" % beta_file)
    beta_df = pd.read_csv(
        beta_file, sep=delimiter, index_col=0, engine='python')

    # Imputate input beta values
    beta_df = impute_beta(beta_df, method=imputation_method, ref=ext_file)
    (n_cpg, n_sample) = beta_df.shape
    logging.info(
        "Input file: \"%s\", Number of CpGs: %d, Number of samples: %d" %
        (beta_file, n_cpg, n_sample))
    all_CpGs = np.array(beta_df.index)

    # Read meta information file
    logging.info("Read meta information file: \"%s\"" % metafile)
    meta_df = pd.read_csv(metafile, sep=None, index_col=0, engine='python')
    meta_df.index = meta_df.index.astype(str)
    # change column names into lower case
    meta_df.columns = meta_df.columns.str.lower()

    if 'age' not in meta_df.columns:
        logging.error(
            "There must be a column named 'age' (case insensitive) in \"%s\""
            % beta_file)
        sys.exit(0)

    if 'designation' not in meta_df.columns:
        logging.warning(
            "Did not find the 'designation' (case insensitive) column in \
            \"%s\". Split samples into %d folds." % (beta_file, cv_folds))
        split_label = False
    else:
        logging.info(
            "Split samples into training and testing sets ...")
        split_label = True

    if split_label:
        train_meta_df = meta_df.loc[
            meta_df['designation'].str.lower() == 'train']
        test_meta_df = meta_df.loc[
            meta_df['designation'].str.lower() == 'test']

        train_sample_ids = np.array(train_meta_df.index)
        train_sample_ages = np.array(train_meta_df['age'])
        train_beta_values = beta_df[train_sample_ids].to_numpy()
        logging.info(
            "%d samples are included in training set: %s ..." %
            (len(train_sample_ids), ', '.join(train_sample_ids[0:5]))
            )

        test_sample_ids = np.array(test_meta_df.index)
        test_sample_ages = np.array(test_meta_df['age'])
        test_beta_values = beta_df[test_sample_ids].to_numpy()
        logging.info(
            "%d samples are included in testing set: %s ..." %
            (len(test_sample_ids), ', '.join(test_sample_ids[0:5]))
            )

        # get the absolute value of the correlation coefficient
        logging.info("Calculate pearson correlation coefficients ...")
        abs_pcc_coefficients = abs(
            pearson_correlation(train_beta_values, train_sample_ages))

        # return list of site indices with a high absolute correlation
        # coefficient
        selected_CpGs_indices = np.where(abs_pcc_coefficients > pcc_cut)[0]
        selected_CpGs = all_CpGs[selected_CpGs_indices]
        logging.info(
            "%d CpG sites are selected: %s ..." %
            (len(selected_CpGs_indices), ', '.join(selected_CpGs[0:5]))
            )

        logging.info(
            "Save beta values of selected CpGs to \"%s\"" % train_cpg_out)
        # beta_df.loc[selected_CpGs].to_csv(cpg_out, sep="\t")
        beta_df[train_sample_ids].iloc[selected_CpGs_indices].to_csv(
            train_cpg_out, sep="\t")

        logging.info(
            "Save beta values of selected CpGs to \"%s\"" % test_cpg_out)
        # beta_df.loc[selected_CpGs].to_csv(cpg_out, sep="\t")
        beta_df[test_sample_ids].iloc[selected_CpGs_indices].to_csv(
            test_cpg_out, sep="\t")

        # initialize the EPM model
        logging.info("Initialize the EPM model ...")
        epm_cv = EpigeneticPacemakerCV(
            iter_limit=iter_n,
            error_tolerance=error_tol,
            cv_folds=cv_folds)

        # fit the model using the training data
        logging.info("Fit the EPM model using training data ...")
        epm_cv.fit(
            train_beta_values[selected_CpGs_indices, :],
            train_sample_ages)

        logging.info("Get training sample EPM predictions (when left out) ...")
        train_predict = epm_cv.predicted_states
        train_out = train_meta_df.assign(
            epm_age=pd.Series(train_predict, index=train_meta_df.index))
        logging.info(
            "Save predicted EPM ages of traning samples to \"%s\""
            % train_age_out)
        train_out.to_csv(train_age_out, sep="\t")

        # generate predicted ages for testing samples
        logging.info("Predict testing samples ...")
        test_predict = epm_cv.predict(
            test_beta_values[selected_CpGs_indices, :])

        test_out = test_meta_df.assign(
            epm_age=pd.Series(test_predict, index=test_meta_df.index))
        # print(test_out)
        logging.info(
            "Save predicted EPM age of testing samples to \"%s\""
            % test_age_out)
        test_out.to_csv(test_age_out, sep="\t")

        logging.info(
            "Generate scatter plot of test samples and save to \"%s\""
            % test_png_out)
        plot_known_predicted_ages(
            known_ages=test_sample_ages,
            predicted_ages=test_predict,
            outfile=test_png_out,
            title="EPM CV predicted ages (testing samples)"
            )
        logging.info(
            "Generate scatter plot of train samples and save to \"%s\""
            % train_png_out)
        plot_known_predicted_ages(
            known_ages=train_sample_ages,
            predicted_ages=train_predict,
            outfile=train_png_out,
            title="EPM CV predicted ages (training samples when left out)"
            )
    # there is no "label column" to designate training/testing samples
    else:
        train_data = meta_df
        train_sample_ids = np.array(train_data.index)
        train_sample_ages = np.array(train_data['age'])
        train_beta_values = beta_df[train_sample_ids].to_numpy()
        logging.info(
            "%d samples are included in training set: %s ..." %
            (len(train_sample_ids), ', '.join(train_sample_ids[0:5]))
            )
        # get the absolute value of the correlation coefficient
        logging.info("Calculate pearson correlation coefficients ...")
        abs_pcc_coefficients = abs(
            pearson_correlation(train_beta_values, train_sample_ages))

        # return list of site indices with a high absolute correlation
        # coefficient
        selected_CpGs_indices = np.where(abs_pcc_coefficients > pcc_cut)[0]
        selected_CpGs = all_CpGs[selected_CpGs_indices]
        logging.info(
            "%d CpG sites are selected: %s ..." %
            (len(selected_CpGs_indices), ', '.join(selected_CpGs[0:5]))
            )

        logging.info(
            "Save beta values of selected CpGs to \"%s\"" % train_cpg_out)
        # beta_df.loc[selected_CpGs].to_csv(cpg_out, sep="\t")
        beta_df[train_sample_ids].iloc[selected_CpGs_indices].to_csv(
            train_cpg_out, sep="\t")

        # initialize the EPM model
        logging.info("Initialize the EPM model ...")
        epm_cv = EpigeneticPacemakerCV(
            iter_limit=iter_n,
            error_tolerance=error_tol,
            cv_folds=cv_folds)

        # fit the model using the training data
        logging.info("Fit the EPM model using training data ...")
        epm_cv.fit(
            train_beta_values[selected_CpGs_indices, :],
            train_sample_ages)

        logging.info("Get training sample EPM predictions (when left out) ...")
        train_predict = epm_cv.predicted_states
        train_out = train_data.assign(
            epm_age=pd.Series(train_predict, index=train_data.index))

        # save predicted EMP age
        logging.info(
            "Save predicted EPM ages of traning samples to \"%s\""
            % train_age_out)
        train_out.to_csv(train_age_out, sep="\t")

        # save scatter plot
        logging.info(
            "Generate scatter plot of train samples and save to \"%s\""
            % train_png_out)
        plot_known_predicted_ages(
            known_ages=train_sample_ages,
            predicted_ages=train_predict,
            outfile=train_png_out,
            title="EPM CV predicted ages (training samples when left out)"
            )


def clock_mouse(beta_file, outfile, genome, metafile=None, delimiter=None,
                cname="WLMT", ff='pdf', na_percent=0.2, ovr=False,
                imputation_method=6, ext_file=None):
    """
    Compute mouse DNAm age using four clocks ("WLMT", "YOMT", "Liver", or
    "Blood"). Note that unlike human DNAm clocks, the input DNA methylation
    values (commonly known as beta values) for mouse DNAm clocks are derived
    from RRBS or WGBS, rather than EPIC array data.

    **The CpG ID is represented by chrom and position (see example below)**

    Parameters
    ----------
    beta_file : str
        The input tabular structure file containing DNA methylation data.
        #example of CSV file
        ID,Br0603,Br0607,Br0608
        chr10_111559529,0.86007,0.79695,0.72618
        chr10_115250413,0.74023,0.64148,0.65569
        chr10_118049337,0.76405,0.7559,0.7059
        ...
    outfile : str
        The prefix of out files.
    genome : str
        Must be one of ["mm39", "mm10"].
    metafile : str, optional
        Meta information (e.g., Age, Sex) of samples.
        Example of a meta file
            Sample_ID       Age     Sex
            s16N    65      M
            s36N    60      F
            s45N    61      M
            ...
    delimiter : str, optional
        Character used to separate columns of the input file.
        The default is None
    cname : str, optional
        Clock name. Must be one of ["WLMT", "YOMT", "mmLiver" and "mmBlood"].
        The default is "Levine".
    ff : str, optional
        The figure format. Must be one of ['pdf', 'png'].
        The default is 'pdf'.
    na_percent : float, optional
        The maximum of percent of missing values.
        The default is 0.2 (20%).
    ovr : bool, optional
        If set, over write existing files. The default is False
    imputation_method : int
        Must be one of [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. See
        imputation.py for details. default is 6.
    ext_file : str
        This is must be exisit if imputation_method is set to 10.
        Two-column, Tab or comma separated file: 1st column is CpG ID, the 2nd
        column is beta value.


    Returns
    -------
    Pandas Series.
    """

    # set up the prefix for output files.
    if outfile is not None:
        out_prefix = outfile
    else:
        out_prefix = cname + '_out'
    logging.info(
        "The prefix of output files is set to \"%s\"." % out_prefix)

    used_cpg_out = out_prefix + '.predictorCpG_found.tsv'
    missed_cpg_out = out_prefix + '.predictorCpG_missed.tsv'
    age_out = out_prefix + '.DNAm_age.tsv'
    coef_out = out_prefix + '.predictorCpG_coef.tsv'
    r_out = out_prefix + '.plots.R'

    if ff.lower() in ['pdf', 'png']:
        figure_out = out_prefix + '.coef_plot.' + ff.lower()
        scatter_out = out_prefix + '.scatter_plot.' + ff.lower()
    else:
        logging.error("Does not suppor format: %s!" % ff)
        sys.exit(0)
    outfiles = [used_cpg_out, missed_cpg_out, age_out, coef_out, r_out,
                figure_out, scatter_out]

    if ovr is True:
        logging.warning(
            "Over write existing files with prefix: %s" % out_prefix)
        for tmp in outfiles:
            try:
                os.remove(tmp)
            except FileNotFoundError:
                continue
    else:
        for tmp in outfiles:
            if os.path.exists(tmp):
                logging.error(
                    "%s exists! Use different prefix or specify \
                    \"--overwrite\" to replace existing files." % tmp)
                sys.exit(0)

    logging.info("Loading %s clock data ..." % cname)
    if cname.lower() == 'mmliver':
        if genome == 'mm10':
            fh = importlib.resources.open_binary('dmc.data', 'liver_mm10.pkl')
        elif genome == 'mm39':
            fh = importlib.resources.open_binary('dmc.data', 'liver_mm39.pkl')
        else:
            logging.error(
                "Cannot find model file for %s (%s)" % (cname, genome))
            sys.exit(0)
    elif cname.lower() == 'mmblood':
        if genome == 'mm10':
            fh = importlib.resources.open_binary('dmc.data', 'blood_mm10.pkl')
        elif genome == 'mm39':
            fh = importlib.resources.open_binary('dmc.data', 'blood_mm39.pkl')
        else:
            logging.error(
                "Cannot find model file for %s (%s)" % (cname, genome))
            sys.exit(0)
    elif cname.lower() == 'wlmt':
        if genome == 'mm10':
            fh = importlib.resources.open_binary('dmc.data', 'WLMT_mm10.pkl')
        elif genome == 'mm39':
            fh = importlib.resources.open_binary('dmc.data', 'WLMT_mm39.pkl')
        else:
            logging.error(
                "Cannot find model file for %s (%s)" % (cname, genome))
            sys.exit(0)
    elif cname.lower() == 'yomt':
        if genome == 'mm10':
            fh = importlib.resources.open_binary('dmc.data', 'YOMT_mm10.pkl')
        elif genome == 'mm39':
            fh = importlib.resources.open_binary('dmc.data', 'YOMT_mm39.pkl')
        else:
            logging.error(
                "Cannot find model file for %s (%s)" % (cname, genome))
            sys.exit(0)
    else:
        logging.error("Unknown command %s" % cname)
        sys.exit(0)

    clock_dat = pickle.load(fh)

    logging.info("Clock's name: \"%s\"" % clock_dat.name)
    logging.info(
        "Clock was trained from: \"%s\"" % ','.join(clock_dat.tissues))
    logging.info("Clock's unit: \"%s\"" % clock_dat.unit)
    logging.info("Number of CpGs used: %d" % clock_dat.ncpg)
    logging.info("Clock's description: \"%s\"" % clock_dat.info)
    clock_coef = pd.Series(clock_dat.coef, name='Coef')
    if cname.lower() == 'wlmt' or cname.lower() == 'mmliver':
        clock_intercept = clock_dat.Intercept
    else:
        clock_intercept = 0.0

    logging.info("Read input file: \"%s\"" % beta_file)
    input_df1 = pd.read_csv(beta_file, sep=None, index_col=0, engine='python')

    # For WLMT clock, the input beta values should be in [0, 100] range
    # convert (0, 1) to (0, 100) for WLMT if needed
    if cname.lower() == 'wlmt' and input_df1.max(axis=None) <= 1:
        logging.info("Change the range of beta values from (0, 1) to (0, 100)")
        input_df1 = input_df1*100
    # For YOMT/mmBlood/mmLiver clock, the input beta values should be in the
    # [0, 1] range. Convert (0, 100) to (0, 1) for YOMT if needed
    if cname.lower() in ('yomt', 'mmliver', 'mmblood') and input_df1.max(axis=None) > 1:
        logging.info("Change the range of beta values from (0, 1) to (0, 100)")
        input_df1 = input_df1/100

    input_df2 = impute_beta(input_df1, method=imputation_method, ref=ext_file)
    (n_cpg, n_sample) = input_df2.shape
    logging.info(
        "Input file: \"%s\", Number of CpGs: %d, Number of samples: %d" %
        (beta_file, n_cpg, n_sample))
    sample_cpg_ids = input_df2.index
    # sample_names = df2.columns

    # printlog("Standardization ...")
    # scaled_df2 = (input_df2 - input_df2.mean())/input_df2.std()

    logging.info("Extract clock CpGs ...")
    # clock CpGs missed from data file
    missed_cpgs = set(clock_coef.index) - set(sample_cpg_ids)
    logging.info(
        "Clock CpGs missed from '%s': %d (%f%%)" %
        (beta_file, len(missed_cpgs), len(missed_cpgs)*100/clock_dat.ncpg))

    if len(missed_cpgs)/clock_dat.ncpg > na_percent:
        logging.critical(
            "Missing clock CpGs exceed %f%%. Exit!" % (na_percent*100))
        sys.exit(0)

    common_cpgs = list(set(clock_coef.index) & set(sample_cpg_ids))
    logging.info(
        "Clock CpGs exisit in \"%s\": %d" % (beta_file, len(common_cpgs)))

    used_df = input_df2.loc[common_cpgs]
    used_clock_coef = clock_coef.loc[common_cpgs]
    (usable_cpg, usable_sample) = used_df.shape
    logging.info(
        "Used CpGs: %d, Used samples: %d" % (usable_cpg, usable_sample))

    df4 = used_df.mul(used_clock_coef, axis=0)

    # df4.to_csv('df4.csv')
    if cname.lower() == 'wlmt':
        output = df4.sum(axis=0) + clock_intercept
    elif cname.lower() == 'mmliver':
        output = 2**(df4.sum(axis=0) + clock_intercept)
    elif cname.lower() == 'mmblood':
        a = 0.1666
        b = 0.4185
        c = -1.712
        output = ((df4.sum(axis=0) - c)/a) ** (1/b)
    elif cname.lower() == 'yomt':
        a = 0.1207
        b = 1.2424
        c = 2.5440
        output = 7*np.exp(a*((df4.sum(axis=0)**2)) + b*df4.sum(axis=0) + c)
    else:
        logging.error("Unknown command %s" % cname)
        sys.exit()
    output.name = "%s" % cname

    if metafile is not None:
        logging.info("Read meta information file: \"%s\"" % metafile)
        meta_df = pd.read_csv(metafile, sep=None, index_col=0, engine='python')
        meta_df.index = meta_df.index.astype(str)
        # combine predicted age and other meta information
        logging.info("Combining meta information with predicted age")
        output = pd.concat([output, meta_df], axis=1)

        # generate scatter plot between c_age and d_age
        c_age = []
        for col_id in output.columns:
            if col_id.lower() == 'age':
                c_age = output[col_id]
                break
        d_age = output[cname]

        if len(c_age) >= 2 and len(c_age) == len(d_age):
            logging.info(
                "Writing R script of scatter plot. Save to: %s" % r_out)
            plot_corr(c_age, d_age, outfile=scatter_out, rfile=r_out)

    # save used CpGs to file
    logging.info("Save used CpGs and beta values to: %s" % used_cpg_out)
    used_df.to_csv(used_cpg_out, sep="\t", index_label="CpG_ID")

    # save missed CpGs to file
    logging.info("Save missed CpGs: %s" % missed_cpg_out)
    tmp = pd.DataFrame(list(missed_cpgs), columns=["missed_CpGs"])
    tmp.to_csv(missed_cpg_out, sep="\t", index=False)

    # save coef information
    logging.info("Save CpG and coefficients to: %s" % coef_out)
    tmp = clock_coef.to_frame()
    tmp['Found'] = tmp.index.isin(common_cpgs)
    tmp.to_csv(coef_out, sep="\t", index_label="CpG_ID")

    # save predicted age
    logging.info("Save predicted DNAm age to: %s" % age_out)
    output.to_csv(age_out, sep="\t", index_label="Sample_ID")

    # generate coefficient plot
    logging.info("Generate coefficient plot. Save to: %s" % figure_out)
    plot_coef(coef_out, figure_out, r_out)

    logging.info("Running R script: %s" % r_out)
    try:
        subprocess.call("Rscript " + r_out, shell=True)
    except subprocess.CalledProcessError as e:
        print("Cannot generate pdf file from " + r_out, file=sys.stderr)
        print(e.output, file=sys.stderr)
        pass
    return output
