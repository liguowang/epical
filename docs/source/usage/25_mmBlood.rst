mmBlood
=======

.. csv-table::
   :widths: 25, 55

   "Predictor CpGs", "90"
   "Unit", "Day"
   "Target Tissue", "Blood"
   "Target Population", "Mouse"
   "Method", "Elastic Net regression"
   "Reference", "`Petkovich DA, Cell Metab. (2017). <https://pubmed.ncbi.nlm.nih.gov/28380383/>`_"
   "Alias", ""

Usage
-----
.. code-block:: text

 usage: epical mmBlood  [-h] [-o out_prefix] [-g {mm10,mm39}] [-p PERCENT]
                        [-d DELIMITER] [-f {pdf,png}] [-m meta_file] [-l log_file]
                        [--impute {-1,0,1,2,3,4,5,6,7,8,9,10}] [-r ref_file]
                        [--debug] [--overwrite]
                        Input_file

 positional arguments:
   Input_file            The input tabular structure file containing DNA
                         methylation data. This filemust have a header row,
                         which contains the names or labels for samples
                         Thefirst column of this file should contain CpG IDs.
                         The remaining cells in thefile should contain DNA
                         methylation beta values, represented as floating-
                         pointnumbers between 0 and 1. Use a TAB, comma, or any
                         other delimiter to separatethe columns. Use 'NaN' or
                         'NA' to represent missing values. This file can be a
                         regular text file or compressed file (".gz", ".Z",
                         ".z", ".bz", ".bz2", ".bzip2").

 options:
   -h, --help            show this help message and exit
   -o out_prefix, --output out_prefix
                         The PREFIX of output files. If no PREFIX is provided,
                         the default prefix "clock_name_out" is used. The
                         generated output files include:
                         "<PREFIX>.DNAm_age.tsv": This file contains the
                         predicted DNAm age. "<PREFIX>.used_CpGs.tsv": This
                         file lists the CpGs that were used to calculate the
                         DNAm age. "<PREFIX>.missed_CpGs.txt": This file
                         provides a list of clock CpGs that were missed or
                         excluded from the input file. "<PREFIX>.coef.tsv":
                         This file contains a list of clock CpGs along with
                         their coefficients. The last column indicates whether
                         the CpG is included in the calculation.
                         "<PREFIX>.plots.R": This file is an R script used to
                         generate visualization plots.
                         "<PREFIX>.coef_plot.pdf": This file is the coefficient
                         plot in either PDF or PNG format.
   -g {mm10,mm39}, --genome {mm10,mm39}
                         The reference genome for Mouse (Mus musculus) used for
                         RRBS or WGBS reads alignment. Must be 'mm10' or
                         'mm39'. default is 'mm10'.
   -p PERCENT, --percent PERCENT
                         The maximum allowable percentage of missing CpGs. Set
                         to 0.2 (20%) by default, which means that if more than
                         20% of the clock CpGs are missing, the estimation of
                         DNAm age cannot be performed.
   -d DELIMITER, --delimiter DELIMITER
                         Separator (usually TAB or comma) used in the input
                         file. If the separator is not provided, the program
                         will automatically detect the separator.
   -f {pdf,png}, --format {pdf,png}
                         The output plot format must be either 'pdf' or 'png'.
                         The default format is 'pdf'.".
   -m meta_file, --metadata meta_file
                         This file contains the meta information for each
                         sample. This file must have a header row, which
                         contains the names or labels for variables (such as
                         "Sex", "Age"). If the header row includes an "Age"
                         column, a scatter plot will be generated to display
                         the correlation between chronological age and
                         predicted DNAm age. The first column of this file
                         should contain sample IDs. The default value is None,
                         indicating that no meta information file is provided.
   -l log_file, --log log_file
                         This file is used to save the log information. By
                         default, if no file is specified (None), the log
                         information will be printed to the screen.
   --impute {-1,0,1,2,3,4,5,6,7,8,9,10}
                         The imputation method code must be one of the 12
                         digits including (-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                         10). The interpretations are: -1: Remove CpGs with any
                         missing values. 0: Fill all missing values with '0.0'.
                         1: Fill all missing values with '1.0'. 2: Fill the
                         missing values with **column mean** 3: Fill the
                         missing values with **column median** 4: Fill the
                         missing values with **column min** 5: Fill the missing
                         values with **column max** 6: Fill the missing values
                         with **row mean** 7: Fill the missing values with
                         **row median** 8: Fill the missing values with **row
                         min** 9: Fill the missing values with **row max** 10:
                         Fill the missing values with **external reference** If
                         10 is specified, an external reference file must be
                         provided.
   -r ref_file, --ref ref_file
                         The external reference file contains two columns,
                         separated by either tabs or commas. The first column
                         represents the probe ID, while the second column
                         contains the corresponding beta values.
   --debug               If set, print detailed information for debugging.
   --overwrite           If set, over-write existing output files.

Example
-------

``$ epical mmBlood Test7_mouse_N81_RRBS_beta.tsv -g mm10 -o mmBlood_out``


.. code-block:: text
 
 2024-04-12 12:15:32 [INFO]  The prefix of output files is set to "mmBlood_out".
 2024-04-12 12:15:32 [INFO]  Loading mmBlood clock data ...
 2024-04-12 12:15:32 [INFO]  Clock's name: "blood_mm10"
 2024-04-12 12:15:32 [INFO]  Clock was trained from: "Blood"
 2024-04-12 12:15:32 [INFO]  Clock's unit: "day"
 2024-04-12 12:15:32 [INFO]  Number of CpGs used: 90
 ...