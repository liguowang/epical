#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:19:26 2022
"""

import pickle
from itertools import islice
import importlib.resources


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


def clockinfo(infile):
    """
    Load a pickle file (CpG clock data) and print its content.

    Parameters
    ----------
    infile : pickle
        Pickle file.

    Returns
    -------
    None

    """
    fh = importlib.resources.open_binary('dmc.data', infile)
    dat = pickle.load(fh)
    # print (dat.name)
    # print ("  Tissues:\t%s" % ','.join(dat.tissues))
    # print ("  Time unit:\t%s" % dat.unit)
    # print ("  CpGs and coefs:\t", take(3, dat.coef.items()))
    # print ("  Total_CpG:\t%d" % dat.ncpg)
    # print ("  Intercept:\t%d" % dat.Intercept)
    # print ("  Information:\t%s" % dat.info)
    # print ("  Method:\t%s" % dat.method)
    # print ("  Reference:\t", dat.ref)
    # print ("  Pub_link:\t%s" % dat.pubmed)
    # print ('\n')
    information = f'Description: {dat.info} Method: {dat.method} Tissue: {dat.tissues}. Used CpGs: {dat.ncpg}. Reference: {dat.ref} PubMed: {dat.pubmed}'
    return information


if __name__ == '__main__':
    clockinfo('GA_Bohlin.pkl')
    clockinfo('GA_Haftorn.pkl')
    clockinfo('GA_Knight.pkl')
    clockinfo('GA_Mayne.pkl')
    clockinfo('GA_Lee_RPC.pkl')
    clockinfo('GA_Lee_CPC.pkl')
    clockinfo('GA_Lee_refined_RPC.pkl')

    clockinfo('Hannum.pkl')
    clockinfo('Horvath_2013.pkl')
    clockinfo('Horvath_2018.pkl')
    clockinfo('Lu_DNAmTL.pkl')
    clockinfo('Levine.pkl')
    clockinfo('Ped_McEwen.pkl')
    clockinfo('Ped_Wu.pkl')
    clockinfo('Zhang_BLUP.pkl')
    clockinfo('Zhang_EN.pkl')
    clockinfo('AltumAge_cpg.pkl')
