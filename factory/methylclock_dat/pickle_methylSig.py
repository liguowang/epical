#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:55:14 2022

@author: m102324

Make pickle files from TSV files.
"""

import pickle
from dmc.methyldat import MakeMethylObj


def make_pickle_file():
    """
    Make pickle files from TSV files.

    Returns
    -------
    None.
    """
    Zhang_BLUP = MakeMethylObj(
        signature_file='coefBlup.tsv',
        signature_name='Zhang_BLUP',
        tissues=['blood', 'saliva'],
        unit='years',
        signature_info='This clock was trained from 13,402 blood and 259 saliva samples, using the Best Linear Unbiased Prediction (BLUP) method.',
        reference='Zhang, Qian et al. “Improved precision of epigenetic clock estimates across tissues and its implication for biological ageing.” Genome medicine (2019).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/31443728/.',
        method='Best Linear Unbiased Prediction (BLUP).'
        )

    Zhang_EN = MakeMethylObj(
        signature_file='coefEN.tsv',
        signature_name='Zhang_EN',
        tissues=['blood', 'saliva'],
        unit='years',
        signature_info='This clock was trained from 13,402 blood and 259 saliva samples, using the Elastic Net (EN) regression.',
        reference='Zhang, Qian et al. “Improved precision of epigenetic clock estimates across tissues and its implication for biological ageing.” Genome medicine (2019).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/31443728/.',
        method='Elastic net regression.'
        )

    Horvath13 = MakeMethylObj(
        signature_file='coefHorvath.tsv',
        signature_name='Horvath13',
        tissues=['Pan-tissue'],
        unit='years',
        signature_info='This clock (Horvath multiple tissue age clock) was trained from 8,000 samples (82 Illumina DNA methylation array datasets, encompassing 51 healthy tissues and cell types).',
        reference='Horvath, Steve. “DNA methylation age of human tissues and cell types.” Genome biology (2013).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/24138928/.',
        method='Elastic Net regression.'
        )

    Horvath13_shrunk = MakeMethylObj(
        signature_file='coefHorvath_shrunk.tsv',
        signature_name='Horvath13_shrunk',
        tissues=['Pan-tissue'],
        unit='years',
        signature_info='This clock (Horvath multiple tissue age clock, shrunk version) was trained from 8,000 samples (82 Illumina DNA methylation array datasets, encompassing 51 healthy tissues and cell types).',
        reference='Horvath, Steve. “DNA methylation age of human tissues and cell types.” Genome biology (2013).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/24138928/.',
        method='Elastic Net regression.'
        )

    Horvath18 = MakeMethylObj(
        signature_file='coefSkin.tsv',
        signature_name='Horvath18',
        tissues=['fibroblasts', 'keratinocytes', 'buccal cells', 'endothelial cells', 'lymphoblastoid cells', 'skin', 'blood', 'saliva'],
        unit='years',
        signature_info ='This clock (Horvath skin & blood clock) was trained from 2,222 samples (age 0 to 92).',
        reference ='Horvath, Steve et al. “Epigenetic clock for skin and blood cells applied to Hutchinson Gilford Progeria Syndrome and ex vivo studies.” Aging (2018).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/30048243/.',
        method='Elastic Net regression.'
        )

    Hannum = MakeMethylObj(
        signature_file='coefHannum.tsv',
        signature_name='Hannum',
        tissues=['whole blood'],
        unit='years',
        signature_info ='This clock (Hannum clock) was trained from the whole blood of 656 human individuals (aged 19 to 101).',
        reference='Hannum, Gregory et al. “Genome-wide methylation profiles reveal quantitative views of human aging rates.” Molecular cell (2013).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/23177740/',
        method='Elastic Net regression.'
        )

    Levine = MakeMethylObj(
        signature_file='coefLevine.tsv',
        signature_name='Levine',
        tissues=['whole blood'],
        unit='years',
        signature_info ='This clock (DNAm PhenoAge) was trained from blood samples of 9926 adults.',
        reference='Levine, Morgan E et al. “An epigenetic biomarker of aging for lifespan and healthspan.” Aging (2018).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/29676998/.',
        method='Elastic Net regression.'
        )

    Lu_DNAmTL = MakeMethylObj(
        signature_file='coefTL.tsv',
        signature_name='Lu_DNAmTL',
        tissues=['blood'],
        unit='Kilobase',
        signature_info ='This clock (DNA methylation estimator of telomere length, or DNAmTL) was trained from 2,256 blood samples.',
        reference='Lu, Ake T et al. “DNA methylation-based estimator of telomere length.” Aging (2019).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/31422385/.',
        method='Elastic Net regression.'
        )

    GA_Bohlin = MakeMethylObj(
        signature_file='coefBohlin.tsv',
        signature_name='Bohlin_gestational',
        tissues=['cord blood'],
        unit='weeks',
        signature_info ='This gestational age clock trained from 1068 cord blood samples collected from the Norwegian Mother and Child Birth Cohort study (MoBa).',
        reference='Bohlin, J et al. “Prediction of gestational age based on genome-wide differentially methylated regions.” Genome biology (2016).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/27717397/.',
        method='Lasso regression.'
        )

    GA_Haftorn = MakeMethylObj(
        signature_file='coefEPIC.tsv',
        signature_name='Haftorn_gestational',
        tissues=['cord blood'],
        unit='weeks',
        signature_info ='This gestational age clock was trained from 755 randomly selected non-ART (assisted reproductive technologies) newborns cord blood samples from the Norwegian Study of Assisted Reproductive Technologies (START)--a substudy of the Norwegian Mother, Father, and Child Cohort Study (MoBa).', \
        reference='Haftorn, Kristine L et al. “An EPIC predictor of gestational age and its application to newborns conceived by assisted reproductive technologies.” Clinical epigenetics (2021).', 
        pub_link='https://pubmed.ncbi.nlm.nih.gov/33875015/.',
        method='Lasso regression.'
        )

    GA_Knight = MakeMethylObj(
        signature_file='coefKnightGA.tsv',
        signature_name='Knight_gestational',
        tissues=['neonatal cord blood', 'blood spot'],
        unit='weeks',
        signature_info ='This gestational age clock was trained from 207 cord blood samples (six independent cohorts) with gestational age from 24 to 42 weeks.',
        reference='Knight, Anna K et al. “An epigenetic clock for gestational age at birth based on blood methylation data.” Genome biology (2016)',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/27717399/.',
        method='Elastic Net regression.'
        )

    GA_Lee_RPC = MakeMethylObj(
        signature_file='coefLee_RPC.tsv',
        signature_name='Lee_gestational_RPC',
        tissues=['placental'],
        unit='weeks',
        signature_info ='This gestational age clock (robust placental clock, RPC)) was trained from 1,102 placental tissue samples. This clock is unaffected by common pregnancy complications such as gestational diabetes and preeclampsia.',
        reference='Lee, Yunsung et al. “Placental epigenetic clocks: estimating gestational age using placental DNA methylation levels.” Aging (2019).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/31235674/.',
        method='Elastic Net regression.'
        )

    GA_Lee_CPC = MakeMethylObj(
        signature_file='coefLee_CPC.tsv',
        signature_name='Lee_gestational_CPC',
        tissues=['placental'],
        unit='weeks',
        signature_info ='This gestational age clock (control placental clock, CPC) was trained from 1,102 placental tissue samples. This clock was trained using placental samples from pregnancies without known placental pathology.',
        reference='Lee, Yunsung et al. “Placental epigenetic clocks: estimating gestational age using placental DNA methylation levels.” Aging (2019).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/31235674/.',
        method='Elastic Net regression.'
        )

    GA_Lee_refined_RPC = MakeMethylObj(
        signature_file='coefLee_refined_RPC.tsv',
        signature_name='Lee_gestational_refined_RPC',
        tissues=['placental'],
        unit='weeks',
        signature_info ='This gestational age clock (refined robust placental clock, refined RPC) was trained from 1,102 placental tissue samples. This clock is for uncomplicated term pregnancies.',
        reference='Lee, Yunsung et al. “Placental epigenetic clocks: estimating gestational age using placental DNA methylation levels.” Aging (2019).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/31235674/.',
        method='Elastic Net regression.'
        )

    GA_Mayne = MakeMethylObj(
        signature_file='coefMayneGA.tsv',
        signature_name='Mayne_gestational',
        tissues=['placental'],
        unit='weeks',
        signature_info ='This gestational age clock was trained from 409 placental tissues with gestational age from 8 to 42 weeks.',
        reference='Mayne, Benjamin T et al. “Accelerated placental aging in early onset preeclampsia pregnancies identified by DNA methylation.” Epigenomics (2017).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/27894195/.',
        method='Elastic Net regression.'
        )

    PedPE = MakeMethylObj(
        signature_file='coefPedBE.tsv',
        signature_name='McEwen_PedPE',
        tissues=['buccal cells'],
        unit='years',
        signature_info ='This clock (Pediatric-Buccal-Epigenetic clock, or PedBE clock) was trained from 1,032 buccal epithelial swab samples (age 0 to 20). Prediction uses the Elastic net regression.',
        reference='McEwen, Lisa M et al. “The PedBE clock accurately estimates DNA methylation age in pediatric buccal cells.” PNAS (2020).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/31611402/.',
        method='Elastic Net regression.'
        )

    Ped_Wu = MakeMethylObj(
        signature_file='coefWu.tsv',
        signature_name='Wu_Children',
        tissues=['blood', 'saliva'],
        unit='years',
        signature_info ='This clock was trained from 716 blood samples (children, age 9 to 212 months old).',
        reference='Wu, Xiaohui et al. “DNA methylation profile is a quantitative measure of biological aging in children.” Aging (2019).',
        pub_link='https://pubmed.ncbi.nlm.nih.gov/31756171/.',
        method='Elastic Net regression.'
        )

    AltumAge = MakeMethylObj(
        signature_file='AltumAge.tsv',
        signature_name='AltumAge',
        tissues=['Pan-tissue'],
        unit='years',
        signature_info ='A deep neural network trained from 142 different experiments using 20318 CpG sites.',
        reference='LP de Lima Camillo et al. “A pan-tissue DNA-methylation epigenetic clock based on deep learning.” Aging (2022).',
        pub_link='https://www.nature.com/articles/s41514-022-00085-y',
        method='Deep neural network.'
        )

    CorticalClock = MakeMethylObj(
        signature_file='coefCorticalClock.tsv',
        signature_name='CorticalClock',
        tissues=['brain cortex'],
        unit='years',
        signature_info ='Epigenetic clock built specifically for human cortex tissue.',
        reference='Shireby GL, et al. "Recalibrating the epigenetic clock: implications for assessing biological age in the human cortex". Brain (2020).',
        pub_link='https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7805794/',
        method='Elastic Net regression.'
        )
    
    with open('Zhang_BLUP.pkl', 'wb') as f:
        pickle.dump(Zhang_BLUP, f)
    with open('Zhang_EN.pkl', 'wb') as f:
        pickle.dump(Zhang_EN, f)
    with open('Horvath13.pkl', 'wb') as f:
        pickle.dump(Horvath13, f)
    with open('Horvath13_shrunk.pkl', 'wb') as f:
        pickle.dump(Horvath13_shrunk, f)
    with open('Horvath18.pkl', 'wb') as f:
        pickle.dump(Horvath18, f)
    with open('Levine.pkl', 'wb') as f:
        pickle.dump(Levine, f)
    with open('Lu_DNAmTL.pkl', 'wb') as f:
        pickle.dump(Lu_DNAmTL, f)
    with open('GA_Bohlin.pkl', 'wb') as f:
        pickle.dump(GA_Bohlin, f)
    with open('GA_Haftorn.pkl', 'wb') as f:
        pickle.dump(GA_Haftorn, f)
    with open('Hannum.pkl', 'wb') as f:
        pickle.dump(Hannum, f)
    with open('GA_Knight.pkl', 'wb') as f:
        pickle.dump(GA_Knight, f)
    with open('GA_Lee_RPC.pkl', 'wb') as f:
        pickle.dump(GA_Lee_RPC, f)
    with open('GA_Lee_CPC.pkl', 'wb') as f:
        pickle.dump(GA_Lee_CPC, f)
    with open('GA_Lee_refined_RPC.pkl', 'wb') as f:
        pickle.dump(GA_Lee_refined_RPC, f)
    with open('GA_Mayne.pkl', 'wb') as f:
        pickle.dump(GA_Mayne, f)
    with open('Ped_McEwen.pkl', 'wb') as f:
        pickle.dump(PedPE, f)
    with open('Ped_Wu.pkl', 'wb') as f:
        pickle.dump(Ped_Wu, f)
    with open('AltumAge_cpg.pkl', 'wb') as f:
        pickle.dump(AltumAge, f)
    with open('CorticalClock.pkl', 'wb') as f:
        pickle.dump(CorticalClock, f)

if __name__ == '__main__':
    make_pickle_file()
