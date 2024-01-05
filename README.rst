.. image:: https://readthedocs.org/projects/ansicolortags/badge/?version=latest
	:target: https://epical.readthedocs.io/?badge=latest

.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
	:target: https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity

.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
	:target: https://www.python.org/

.. image:: https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg
	:target: https://www.sphinx-doc.org/


Installation
=============

*Epical* is coded in Python. It needs Python 3 (version 3.5.x) or a later
version for installation and execution.

Prerequisites
--------------

- `Python 3 <https://www.python.org/downloads/>`_
- `pip3 <https://pip.pypa.io/en/stable/installing/>`_
- `R <https://www.r-project.org/>`_
- `TensorFlow <https://www.tensorflow.org/>`_ (Only requires by *AltumAge*)

.. note::
   `TensorFlow <https://www.tensorflow.org/>`_ is not included as a Python
   Dependency (refer to the section below) due to its substantial size and
   occasional need for specialized installation procedures. Please follow
   its provided `installation instruction <https://www.tensorflow.org/install>`_
   . Failure to install `TensorFlow <https://www.tensorflow.org/>`_ will result
   in the unavailability of the *AltumAge* command. If you opted for a Python
   virtual environment to install TensorFlow, it is recommend to install
   *Epical* within the same virtual environment.


Python Dependencies
--------------------

- `pandas <https://pandas.pydata.org/>`_
- `numpy <http://www.numpy.org/>`_
- `scipy <https://www.scipy.org/>`_
- `sklearn <https://www.scilearn.com/>`_
- `bx-python <https://github.com/bxlab/bx-python>`_
- `matplotlib <https://matplotlib.org/>`_
- `EpigeneticPacemaker <https://epigeneticpacemaker.readthedocs.io/en/latest/>`_

.. note::
   Users do NOT need to install these packages manually, as they will be
   automatically installed if you use
   `pip3 <https://pip.pypa.io/en/stable/installing/>`_.

Install Epical
--------------
::

 # install from PyPI
 $ pip3 install epical

 # install from github
 $ pip3 install git+https://github.com/liguowang/epical.git

 # test if *epical* is available and excutable
 $ epical --version
 epical 0.0.1

.. note::
   If you used Python virtual environment to install
   `TensorFlow <https://www.tensorflow.org/>`_, you need to run the
   above command in the same virtual environment.


Upgrade *Epical*
-----------------
::

 $ pip3 install epical --upgrade

Uninstall *Epical*
-------------------
::

$ pip3 uninstall epical

Run *Epical*
------------
::

 $ epical --help
 usage: epical [-h] [-v]
              {Horvath13,Horvath13_shrunk,Horvath18,Levine,Hannum,Zhang_EN,Zhang_BLUP,AltumAge,Lu_DNAmTL,Ped_Wu,PedPE,GA_Bohlin,GA_Haftorn,GA_Knight,GA_Mayne,GA_Lee_CPC,GA_Lee_RPC,GA_Lee_rRPC,Cortical,EPM}
              ...

 epical : An epigenetic age calculator.

 positional arguments:
  {Horvath13,Horvath13_shrunk,Horvath18,Levine,Hannum,Zhang_EN,Zhang_BLUP,AltumAge,Lu_DNAmTL,Ped_Wu,PedPE,GA_Bohlin,GA_Haftorn,GA_Knight,GA_Mayne,GA_Lee_CPC,GA_Lee_RPC,GA_Lee_rRPC,Cortical,EPM}
                        Sub-command description:
    Horvath13           Description: This clock (Horvath multiple tissue age clock) was trained from 8,000 samples (82 Illumina DNA methylation array
                        datasets, encompassing 51 healthy tissues and cell types). Method: Elastic Net regression. Tissue: ['Pan-tissue']. Used CpGs:
                        353. Reference: Horvath, Steve. “DNA methylation age of human tissues and cell types.” Genome biology (2013). PubMed:
                        https://pubmed.ncbi.nlm.nih.gov/24138928/.
    Horvath13_shrunk    Description: This clock (Horvath multiple tissue age clock, shrunk version) was trained from 8,000 samples (82 Illumina DNA
                        methylation array datasets, encompassing 51 healthy tissues and cell types). Method: Elastic Net regression. Tissue: ['Pan-
                        tissue']. Used CpGs: 110. Reference: Horvath, Steve. “DNA methylation age of human tissues and cell types.” Genome biology
                        (2013). PubMed: https://pubmed.ncbi.nlm.nih.gov/24138928/.
    Horvath18           Description: This clock (Horvath skin & blood clock) was trained from 2,222 samples (age 0 to 92). Method: Elastic Net
                        regression. Tissue: ['fibroblasts', 'keratinocytes', 'buccal cells', 'endothelial cells', 'lymphoblastoid cells', 'skin',
                        'blood', 'saliva']. Used CpGs: 391. Reference: Horvath, Steve et al. “Epigenetic clock for skin and blood cells applied to
                        Hutchinson Gilford Progeria Syndrome and ex vivo studies.” Aging (2018). PubMed: https://pubmed.ncbi.nlm.nih.gov/30048243/.
    Levine              Description: This clock (DNAm PhenoAge) was trained from blood samples of 9926 adults. Method: Elastic Net regression.
                        Tissue: ['whole blood']. Used CpGs: 513. Reference: Levine, Morgan E et al. “An epigenetic biomarker of aging for lifespan
                        and healthspan.” Aging (2018). PubMed: https://pubmed.ncbi.nlm.nih.gov/29676998/.
    Hannum              Description: This clock (Hannum clock) was trained from the whole blood of 656 human individuals (aged 19 to 101). Method:
                        Elastic Net regression. Tissue: ['whole blood']. Used CpGs: 71. Reference: Hannum, Gregory et al. “Genome-wide methylation
                        profiles reveal quantitative views of human aging rates.” Molecular cell (2013). PubMed:
                        https://pubmed.ncbi.nlm.nih.gov/23177740/
    Zhang_EN            Description: This clock was trained from 13,402 blood and 259 saliva samples, using the Elastic Net (EN) regression. Method:
                        Elastic net regression. Tissue: ['blood', 'saliva']. Used CpGs: 514. Reference: Zhang, Qian et al. “Improved precision of
                        epigenetic clock estimates across tissues and its implication for biological ageing.” Genome medicine (2019). PubMed:
                        https://pubmed.ncbi.nlm.nih.gov/31443728/.
    Zhang_BLUP          Description: This clock was trained from 13,402 blood and 259 saliva samples, using the Best Linear Unbiased Prediction
                        (BLUP) method. Method: Best Linear Unbiased Prediction (BLUP). Tissue: ['blood', 'saliva']. Used CpGs: 319607. Reference:
                        Zhang, Qian et al. “Improved precision of epigenetic clock estimates across tissues and its implication for biological
                        ageing.” Genome medicine (2019). PubMed: https://pubmed.ncbi.nlm.nih.gov/31443728/.
    AltumAge            Description: A deep neural network trained from 142 different experiments using 20318 CpG sites. Method: Deep neural network.
                        Tissue: ['Pan-tissue']. Used CpGs: 20318. Reference: LP de Lima Camillo et al. “A pan-tissue DNA-methylation epigenetic clock
                        based on deep learning.” Aging (2022). PubMed: https://www.nature.com/articles/s41514-022-00085-y
    Lu_DNAmTL           Description: This clock (DNA methylation estimator of telomere length, or DNAmTL) was trained from 2,256 blood samples.
                        Method: Elastic Net regression. Tissue: ['blood']. Used CpGs: 140. Reference: Lu, Ake T et al. “DNA methylation-based
                        estimator of telomere length.” Aging (2019). PubMed: https://pubmed.ncbi.nlm.nih.gov/31422385/.
    Ped_Wu              Description: This clock was trained from 716 blood samples (children, age 9 to 212 months old). Method: Elastic Net
                        regression. Tissue: ['blood', 'saliva']. Used CpGs: 111. Reference: Wu, Xiaohui et al. “DNA methylation profile is a
                        quantitative measure of biological aging in children.” Aging (2019). PubMed: https://pubmed.ncbi.nlm.nih.gov/31756171/.
    PedPE               Description: This clock (Pediatric-Buccal-Epigenetic clock, or PedBE clock) was trained from 1,032 buccal epithelial swab
                        samples (age 0 to 20). Prediction uses the Elastic net regression. Method: Elastic Net regression. Tissue: ['buccal cells'].
                        Used CpGs: 94. Reference: McEwen, Lisa M et al. “The PedBE clock accurately estimates DNA methylation age in pediatric buccal
                        cells.” PNAS (2020). PubMed: https://pubmed.ncbi.nlm.nih.gov/31611402/.
    GA_Bohlin           Description: This gestational age clock trained from 1068 cord blood samples collected from the Norwegian Mother and Child
                        Birth Cohort study (MoBa). Method: Lasso regression. Tissue: ['cord blood']. Used CpGs: 96. Reference: Bohlin, J et al.
                        “Prediction of gestational age based on genome-wide differentially methylated regions.” Genome biology (2016). PubMed:
                        https://pubmed.ncbi.nlm.nih.gov/27717397/.
    GA_Haftorn          Description: This gestational age clock was trained from 755 randomly selected non-ART (assisted reproductive technologies)
                        newborns cord blood samples from the Norwegian Study of Assisted Reproductive Technologies (START)--a substudy of the
                        Norwegian Mother, Father, and Child Cohort Study (MoBa). Method: Lasso regression. Tissue: ['cord blood']. Used CpGs: 176.
                        Reference: Haftorn, Kristine L et al. “An EPIC predictor of gestational age and its application to newborns conceived by
                        assisted reproductive technologies.” Clinical epigenetics (2021). PubMed: https://pubmed.ncbi.nlm.nih.gov/33875015/.
    GA_Knight           Description: This gestational age clock was trained from 207 cord blood samples (six independent cohorts) with gestational
                        age from 24 to 42 weeks. Method: Elastic Net regression. Tissue: ['neonatal cord blood', 'blood spot']. Used CpGs: 148.
                        Reference: Knight, Anna K et al. “An epigenetic clock for gestational age at birth based on blood methylation data.” Genome
                        biology (2016) PubMed: https://pubmed.ncbi.nlm.nih.gov/27717399/.
    GA_Mayne            Description: This gestational age clock was trained from 409 placental tissues with gestational age from 8 to 42 weeks.
                        Method: Elastic Net regression. Tissue: ['placental']. Used CpGs: 62. Reference: Mayne, Benjamin T et al. “Accelerated
                        placental aging in early onset preeclampsia pregnancies identified by DNA methylation.” Epigenomics (2017). PubMed:
                        https://pubmed.ncbi.nlm.nih.gov/27894195/.
    GA_Lee_CPC          Description: This gestational age clock (control placental clock, CPC) was trained from 1,102 placental tissue samples. This
                        clock was trained using placental samples from pregnancies without known placental pathology. Method: Elastic Net regression.
                        Tissue: ['placental']. Used CpGs: 1125. Reference: Lee, Yunsung et al. “Placental epigenetic clocks: estimating gestational
                        age using placental DNA methylation levels.” Aging (2019). PubMed: https://pubmed.ncbi.nlm.nih.gov/31235674/.
    GA_Lee_RPC          Description: This gestational age clock (robust placental clock, RPC)) was trained from 1,102 placental tissue samples. This
                        clock is unaffected by common pregnancy complications such as gestational diabetes and preeclampsia. Method: Elastic Net
                        regression. Tissue: ['placental']. Used CpGs: 1125. Reference: Lee, Yunsung et al. “Placental epigenetic clocks: estimating
                        gestational age using placental DNA methylation levels.” Aging (2019). PubMed: https://pubmed.ncbi.nlm.nih.gov/31235674/.
    GA_Lee_rRPC         Description: This gestational age clock (refined robust placental clock, refined RPC) was trained from 1,102 placental tissue
                        samples. This clock is for uncomplicated term pregnancies. Method: Elastic Net regression. Tissue: ['placental']. Used CpGs:
                        1125. Reference: Lee, Yunsung et al. “Placental epigenetic clocks: estimating gestational age using placental DNA methylation
                        levels.” Aging (2019). PubMed: https://pubmed.ncbi.nlm.nih.gov/31235674/.
    Cortical            Description: Epigenetic clock built specifically for human cortex tissue. Method: Elastic Net regression. Tissue: ['brain
                        cortex']. Used CpGs: 347. Reference: Shireby GL, et al. "Recalibrating the epigenetic clock: implications for assessing
                        biological age in the human cortex". Brain (2020). PubMed: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7805794/
    EPM                 Description: The Epigenetic Pacemake (EPM), is a fast conditional expectationmaximization algorithm that models epigenetic
                        states under and evolutionaryframework. Unlike the linear regression approach, it does not assume a linearrelationship
                        between the epigenetic state and a trait of interest. Reference:Farrell C, et al. "The Epigenetic Pacemaker: modeling
                        epigenetic states underan evolutionary framework". Bioinformatics (2020). PubMed:https://pubmed.ncbi.nlm.nih.gov/32573701/.
 
 options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit


Documentation
=============
`https://epical.readthedocs.io/en/latest/ <https://epical.readthedocs.io/en/latest/>`_
