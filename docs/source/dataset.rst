Test datasets
==============

We provide three test datasets generated from the human liver, blood, and brain, using Illumina HumanMethylation450 (450K), MethylationEPIC v1.0 (850K), and MethylationEPIC v2.0, respectively.

Liver Dataset
-------------

  * `liver_N32_HumanMethylation450_beta.tsv.gz <https://sourceforge.net/projects/epical/files/liver_N32_HumanMethylation450_beta.tsv.gz/download>`_
  * Sample: Normal liver tissue (no liver diseases)
  * Source: Mayo Clinic
  * Platform: Illumina HumanMethylation450 (450K)
  * Dimension: 485512 CpGs x 32 Samples
  * Chronological age: 49 to 82 years
  * Meta information: `liver_N32_info.tsv <https://sourceforge.net/projects/epical/files/liver_N32_info.tsv/download>`_
 

Blood Dataset
--------------

  * `blood_N20_MethylationEPIC-v1.0_beta.tsv.gz <https://sourceforge.net/projects/epical/files/blood_N20_MethylationEPIC-v1.0_beta.tsv.gz/download>`_
  * Sample: Whole blood from healthy donors 
  * Source: Mayo Clinic
  * Platform: Illumina MethylationEPIC v1.0 (850K)
  * Dimension: 865859 CpGs x 20 Samples
  * Meta information: `blood_N20_info.tsv <https://sourceforge.net/projects/epical/files/blood_N20_info.tsv/download>`_
  * Chronological age: 2 to 81 years 


Brain Tumor Dataset
--------------------

  * `brain_N16_MethylationEPIC-v2.0_beta.tsv.gz <https://sourceforge.net/projects/epical/files/brain_N16_MethylationEPIC-v2.0_beta.tsv.gz/download>`_
  * Sample: Brain tumor patients
  * Source: NCI [1]_
  * Platform: Illumina MethylationEPIC v2.0
  * Dimension: 853304 CpGs x 16 Samples
  * Meta information: `brain_N16_info.tsv <https://sourceforge.net/projects/epical/files/brain_N16_info.tsv/download>`_
  * Chronological age: 0.4 to 77 years

These data are also available from `here <https://drive.google.com/drive/folders/1dYPxWB5lYTNEEYhvjqUjcfp8G-sJBsiC?usp=drive_link>`_

MD5SUM

+--------------------------------------------+----------------------------------+
| File                                       | MD5SUM                           |
+--------------------------------------------+----------------------------------+
| liver_N32_HumanMethylation450_beta.tsv.gz  | a868457bd3d50aadeb5f34d50ef82dc6 |
+--------------------------------------------+----------------------------------+
| liver_N32_info.tsv                         | 79213c1682909a7a02109f3127a0fea3 |
+--------------------------------------------+----------------------------------+
| blood_N20_MethylationEPIC-v1.0_beta.tsv.gz | 528a5896bcaae4a77757c35c7abcd507 |
+--------------------------------------------+----------------------------------+
| blood_N20_info.tsv                         | a19446c8ce35a93d081cda1dedaaece9 |
+--------------------------------------------+----------------------------------+
| brain_N16_MethylationEPIC-v2.0_beta.tsv.gz | ec566e0cf5b5dd48ed4797e132b326dd |
+--------------------------------------------+----------------------------------+
| brain_N16_info.tsv                         | ab06affa9b8ccfa00b05983e30f09775 |
+--------------------------------------------+----------------------------------+

.. [1] Data were downloaded from GEO with accession #: `GSE229715 <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE229715>`_
