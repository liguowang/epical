#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:55:42 2023

"""

general_help = '''
    Epical: A DNA Methylation-Based Epigenetic Age Calculator.
    '''

format_help = '''
    The output plot format must be either 'pdf' or 'png'.
    The default format is 'pdf'.".
    '''

input_help = '''
    The input tabular structure file containing DNA methylation data. This
    filemust have a header row, which contains the names or labels for samples
    Thefirst column of this file should contain CpG IDs. The remaining cells in
    thefile should contain DNA methylation beta values, represented as
    floating-pointnumbers between 0 and 1. Use a TAB, comma, or any other
    delimiter to separatethe columns. Use 'NaN' or 'NA' to represent missing
    values. This file can be a regular text file or compressed file
    (".gz", ".Z", ".z", ".bz", ".bz2", ".bzip2").
    '''

output_help = '''
    The PREFIX of output files. If no PREFIX is provided, the default prefix
    "clock_name_out" is used. The generated output files include:

    "<PREFIX>.DNAm_age.tsv":
        This file contains the predicted DNAm age.
    "<PREFIX>.used_CpGs.tsv":
        This file lists the CpGs that were used to calculate the DNAm age.
    "<PREFIX>.missed_CpGs.txt":
        This file provides a list of clock CpGs that were missed or excluded
        from the input file.
    "<PREFIX>.coef.tsv":
        This file contains a list of clock CpGs along with their coefficients.
        The last column indicates whether the CpG is included in the
        calculation.
    "<PREFIX>.plots.R": This file is an R script used to generate
        visualization plots.
    "<PREFIX>.coef_plot.pdf":
        This file is the coefficient plot in either PDF or PNG format.
    '''

na_help = '''
    The maximum allowable percentage of missing CpGs. Set to 0.2 (20%%) by
    default, which means that if more than 20%% of the clock CpGs are missing,
    the estimation of DNAm age cannot be performed.
'''

del_help = '''
    Separator (usually TAB or comma) used in the input file. If the separator
    is not provided, the program will automatically detect the separator.
    '''

debug_help = '''
    If set, print detailed information for debugging.
    '''

meta_help = '''
    This file contains the meta information for each sample. This file must
    have a header row, which contains the names or labels for variables (such
    as "Sex", "Age"). If the header row includes an "Age" column, a scatter
    plot will be generated to display the correlation between chronological
    age and predicted DNAm age. The first column of this file should contain
    sample IDs. The default value is None, indicating that no meta information
    file is provided.
    '''

epm_meta_help = '''
    This file contains the meta information for each sample. This file must
    have a header row, which contains the names or labels for variables. The
    'Age' variable must exist. The 'Designation' variable is used to designate
    training and testing samples.
    '''

epm_help = '''
    Description: The Epigenetic Pacemake (EPM), is a fast conditional
    expectationmaximization algorithm that models epigenetic states under and
    evolutionaryframework. Unlike the linear regression approach, it does not
    assume a linearrelationship between the epigenetic state and a trait of
    interest. Reference: Farrell C, et al. "The Epigenetic Pacemaker: modeling
    epigenetic states underan evolutionary framework". Bioinformatics (2020).
    PubMed: https://pubmed.ncbi.nlm.nih.gov/32573701/.
    '''

WLMT_help = '''
    Description: WLMT is a whole lifespan, multi-tissue mouse epigenetic age
    predictor based on 435 CpG sites identified from RRBS/WGBS.
    Reference: Meer MV, et al. "A whole lifespan mouse multi-tissue DNA
    methylation clock". Elife (2018).
    Pubmed: https://pubmed.ncbi.nlm.nih.gov/30427307/.
    *Note*: Unlike human DNAm clocks where the beta values are calculated from
    EPIC array data, for mouse clocks, the beta values are derived from RRBS
    or WGBS data. Consequently, in mouse clocks, the IDs of clock CpGs are
    represented in the format of "chrom_position" (where the position indicates
    the 1-based coordinate of 'C'). Furthermore, the range of beta values in
    this clocks is (0, 100) instead of (0, 1). If the input beta values range
    from 0 to 1, they will be automatically converted to the (0, 100) range.
    '''

YOMT_help = '''
    Description: YOMT is a whole lifespan, multi-tissue mouse epigenetic age
    predictor based on 329 CpG sites dentified from RRBS/WGBS.
    Reference: Stubbs TM, et al. "Multi-tissue DNA methylation age predictor
    in mouse". Genome Biol. (2017).
    Pubmed: https://pubmed.ncbi.nlm.nih.gov/28399939/.
    *Note*: Unlike human DNAm clocks where the beta values are calculated from
    EPIC array data, for mouse clocks, the beta values are derived from RRBS
    or WGBS data. Consequently, in mouse clocks, the IDs of clock CpGs are
    represented in the format of "chrom_position" (where the position indicates
    the 1-based coordinate of 'C').
    '''
mmLiver_help = '''
    Description: A mouse epigenetic age predictor based on 148 CpG sites.
    Tissue: ['liver'].
    Reference: Wang T, et al. "Epigenetic aging signatures in
    mice livers are slowed by dwarfism, calorie restriction and rapamycin
    treatment". Genome Biol. (2017).
    Pubmed: https://pubmed.ncbi.nlm.nih.gov/28351423/.
    *Note*: Unlike human DNAm clocks where the beta values are calculated from
    EPIC array data, for mouse clocks, the beta values are derived from RRBS
    or WGBS data. Consequently, in mouse clocks, the IDs of clock CpGs are
    represented in the format of "chrom_position" (where the position indicates
    the 1-based coordinate of 'C').
    '''
mmBlood_help = '''
    Description: A mouse epigenetic age predictor based on 90 CpG
    sites. Tissue: ['blood'].
    Reference: Petkovich DA, et al. "Using DNA Methylation Profiling to
    Evaluate Biological Age and Longevity Interventions". Cell Metab. (2017).
    Pubmed: https://pubmed.ncbi.nlm.nih.gov/28380383/.
    *Note*: Unlike human DNAm clocks where the beta values are calculated from
    EPIC array data, for mouse clocks, the beta values are derived from RRBS
    or WGBS data. Consequently, in mouse clocks, the IDs of clock CpGs are
    represented in the format of "chrom_position" (where the position indicates
    the 1-based coordinate of 'C').
    '''
epm_output_help = '''
    The PREFIX of output files. If no PREFIX is provided, the default prefix
    "EPM_out" is used. The generated output files include:

    "<PREFIX>.test_EPM_age.tsv":
        The predicted EPM age for testing samples.
    "<PREFIX>.train_EPM_age.tsv":
         The predicted EPM age for training samples.
    "<PREFIX>.test_EPM_age.pdf" or "<PREFIX>.test_EPM_age.png:
        Scatter plot showing the trend between the predicted EPM ages and
        chronological ages for testing samples.
    "<PREFIX>.train_EPM_age.pdf" or "<PREFIX>.train_EPM_age.png:
        Scatter plot showing the trend between the predicted EPM ages and
        chronological ages for training samples.
    "<PREFIX>.test_selected_CpGs.tsv":
        Selected feature CpGs and their beta values for testing samples.
    "<PREFIX>.train_selected_CpGs.tsv":
        Selected feature CpGs and their beta values for training samples.
    '''

log_help = '''
    This file is used to save the log information. By default, if no file is
    specified (None), the log information will be printed to the screen.
    '''

imputation_help = '''
    The imputation method code must be one of the 12 digits including (-1,
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10). The interpretations are:
        -1: Remove CpGs with any missing values.
        0: Fill all missing values with '0.0'.
        1: Fill all missing values with '1.0'.
        2: Fill the missing values with **column mean**
        3: Fill the missing values with **column median**
        4: Fill the missing values with **column min**
        5: Fill the missing values with **column max**
        6: Fill the missing values with **row mean**
        7: Fill the missing values with **row median**
        8: Fill the missing values with **row min**
        9: Fill the missing values with **row max**
        10: Fill the missing values with **external reference**
    If 10 is specified, an external reference file must be provided.
    '''

ext_ref_help = '''
    The external reference file contains two columns, separated by either
    tabs or commas. The first column represents the probe ID, while the
    second column contains the corresponding beta values.
    '''
