Overview
========

Introduction
------------

Aging is a multifaceted, time-dependent process influenced by various factors, 
including genetics, lifestyle, nutrition, mental well-being, as well as social 
and environmental conditions. Consequently, the aging speed can significantly 
differ among individuals, rendering **chronological age** (i.e., the number of 
years a person has been alive) an inadequate indicator of a person’s overall 
health status and predictive value for disease onset and treatment responses.
In contrast, **biological (or physiological) age** employs bio-physiological
measurements to more accurately gauge an individual's life clock [1]_ [2]_.

DNA methylation-based biological age estimation has been widely used;
however, a universally applicable bioinformatics tool is currently lacking.
The `Epical <https://github.com/liguowang/epical>`_ package provides a
number of commands to calcuate epigenetic ages from DNA methylation data
generated from Illumina HumanMethylation450 BeadChip (450K), MethylationEPIC
v1.0 (850K) or MethylationEPIC v2.0 array.


Available clocks for Human
---------------------------
.. image:: ./_static/human2.png
   :height: 140 px
   :width: 650 px
   :scale: 100 %  
   :alt: mouse.png


+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
|    | Clock_name                                                          | Predictor CpGs | Unit | Tissue            | Method      |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 1  | `Horvath13 <https://pubmed.ncbi.nlm.nih.gov/24138928/>`_            | 353            | Year | Pan-tissue        | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 2  | `Horvath13_shrunk <https://pubmed.ncbi.nlm.nih.gov/24138928/>`_     | 110            | Year | Pan-tissue        | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 3  | `Horvath18 <https://pubmed.ncbi.nlm.nih.gov/30048243/>`_            | 391            | Year | Skin & blood      | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 4  | `Levine <https://pubmed.ncbi.nlm.nih.gov/29676998/>`_               | 513            | Year | Blood             | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 5  | `Hannum <https://pubmed.ncbi.nlm.nih.gov/23177740/>`_               | 71             | Year | Blood             | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 6  | `Zhang_EN <https://pubmed.ncbi.nlm.nih.gov/31443728/>`_             | 514            | Year | Blood, Saliva     | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 7  | `Zhang_BLUP <https://pubmed.ncbi.nlm.nih.gov/31443728/>`_           | 319607         | Year | Blood, Saliva     | BLUP        |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 8  | `AltumAge <https://www.nature.com/articles/s41514-022-00085-y>`_    | 20318          | Year | Pan-tissue        | DNN         |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 9  | `Cortical <https://pubmed.ncbi.nlm.nih.gov/33300551/>`_             | 347            | Year | Brain cortex      | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 10 | `MEAT <https://pubmed.ncbi.nlm.nih.gov/32067420/>`_                 | 200            | Year | Skeletal muscle   | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 11 | `EPM <https://pubmed.ncbi.nlm.nih.gov/32573701/>`_                  | n/a            | n/a  | n/a               | EM          |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 12 | `Lu_DNAmTL <https://pubmed.ncbi.nlm.nih.gov/31422385/>`_            | 140            | Kb   | Blood             | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 13 | `Ped_Wu <https://pubmed.ncbi.nlm.nih.gov/31756171/>`_               | 111            | Year | Blood             | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 14 | `PedBE <https://pubmed.ncbi.nlm.nih.gov/31611402/>`_                | 94             | Year | Buccal epithelial | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 15 | `GA_Bohlin <https://pubmed.ncbi.nlm.nih.gov/27717397/>`_            | 96             | Day  | Cord blood        | LASSO       |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 16 | `GA_Haftorn <https://pubmed.ncbi.nlm.nih.gov/33875015/>`_           | 176            | Day  | Cord blood        | LASSO       |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 17 | `GA_Knight <https://pubmed.ncbi.nlm.nih.gov/27717399/>`_            | 148            | Week | Cord blood        | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 18 | `GA_Mayne <https://pubmed.ncbi.nlm.nih.gov/27894195/>`_             | 62             | Week | Placental tissues | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 19 | `GA_Lee_CPC <https://pubmed.ncbi.nlm.nih.gov/31235674/>`_           | 546            | Week | Placental tissues | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 20 | `GA_Lee_RPC <https://pubmed.ncbi.nlm.nih.gov/31235674/>`_           | 558            | Week | Placental tissues | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+
| 21 | `GA_Lee_rRPC <https://pubmed.ncbi.nlm.nih.gov/31235674/>`_          | 395            | Week | Placental tissues | Elastic Net |
+----+---------------------------------------------------------------------+----------------+------+-------------------+-------------+


.. note::
   * Input data for these clocks are generated from Illumina 'BeadChip' methylation array.
   * The "EPM" algorithem needs user provide training data.
   * All the commands (i.e. Clock_name) are case-sensitive.


Available clocks for Mouse (*Mus Musculus*)
-------------------------------------------


.. image:: ./_static/mouse.png
   :height: 120 px
   :width: 250 px
   :scale: 100 %  
   :alt: mouse.png

+----+---------------------------------------------------------------+----------------+------+-------------------+-------------+
|    | Clock_name                                                    | Predictor CpGs | Unit | Tissue            | Method      |
+----+---------------------------------------------------------------+----------------+------+-------------------+-------------+
| 1  | `WLMT <https://pubmed.ncbi.nlm.nih.gov/30427307/>`_           | 435            | Day  | Pan-tissue        | Elastic Net |
+----+---------------------------------------------------------------+----------------+------+-------------------+-------------+
| 2  | `YOMT <https://pubmed.ncbi.nlm.nih.gov/28399939/>`_           | 329            | Day  | Pan-tissue        | Elastic Net |
+----+---------------------------------------------------------------+----------------+------+-------------------+-------------+
| 3  | `mmLiver <https://pubmed.ncbi.nlm.nih.gov/28351423/>`_        | 148            | Day  | Liver             | Elastic Net |
+----+---------------------------------------------------------------+----------------+------+-------------------+-------------+
| 4  | `mmBlood <https://pubmed.ncbi.nlm.nih.gov/28380383/>`_        | 90             | Day  | Blood             | Elastic Net |
+----+---------------------------------------------------------------+----------------+------+-------------------+-------------+

.. note::
   * Input data for these clocks are generated from RRBS (Reduced-Representation Bisulfite Sequencing) or WGBS (Whole Genome Bisulfite Sequencing).
   * WLMT = Whole Life Multiple Tissue. This clock was trained from mice aged 6 to 30 months.
   * YOMT = YOung Multiple Tissue. This clock was trained from mice aged 0 to 10 months.


.. [1] Maltoni R, Ravaioli S, Bronte G, et al. "Chronological age or biological age: What drives the choice of adjuvant treatment in elderly breast cancer patients?" Transl Oncol (2022).
.. [2] Rutledge J, Oh H, Wyss-Coray T. "Measuring biological age using omics data". Nat Rev Genet (2022).


