#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:55:42 2023

"""

general_help = '''
    epical : An epigenetic age calculator.
    '''

format_help = '''
    Figure format of the output coef plot. It must be "pdf" or "png".
    The default is "pdf".
    '''

input_help = '''
    The input tabular structure file containing DNA methylation data. This
    filemust have a header row, which contains the names or labels for samples
    Thefirst column of this file should contain CpG IDs. The remaining cells in
    thefile should contain DNA methylation beta values, represented as
    floating-pointnumbers between 0 and 1. Use a TAB, comma, or any other
    delimiter to separatethe columns. Use 'NaN' or 'NA' to represent missing
    values.
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
    interest. Reference:Farrell C, et al. "The Epigenetic Pacemaker: modeling
    epigenetic states underan evolutionary framework". Bioinformatics (2020).
    PubMed:https://pubmed.ncbi.nlm.nih.gov/32573701/.
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
