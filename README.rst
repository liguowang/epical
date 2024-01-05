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
--------------
::
 
 # print out version number and exit.
 $ epical --verion
 epical 0.0.1
 
 # print out usage and all the available clocks
 $ epical --help
  usage: epical [-h] [-v] 
  {Horvath13, Horvath13_shrunk, Horvath18, Levine, ...}
  ...
 
 # print out usage of the "Horvath13" command
 $ epical Horvath13 --help
 
 usage: epical Horvath13 [-h] [-o out_prefix] [-p PERCENT] [-d DELIMITER]
                        [-f {pdf,png}] [-m meta_file] [-l log_file]
                        [--impute {-1,0,1,2,3,4,5,6,7,8,9,10}] [-r ref_file]
                        [--overwrite] [--debug]
                        Input_file

 positional arguments:
  Input_file            The input tabular structure file containing DNA methylation
                        data. This filemust have a header row, which contains the
                        names or labels for samples Thefirst column of this file
                        should contain CpG IDs. The remaining cells in thefile
                        should contain DNA methylation beta values, represented as
                        floating-pointnumbers between 0 and 1. Use a TAB, comma, or
                        any other delimiter to separatethe columns. Use 'NaN' or
                        'NA' to represent missing values.

 options:
  -h, --help            show this help message and exit
  -o out_prefix, --output out_prefix
                        The PREFIX of output files. If no PREFIX is provided, the
                        default prefix "clock_name_out" is used. The generated
                        output files include: "<PREFIX>.DNAm_age.tsv": This file
                        contains the predicted DNAm age. "<PREFIX>.used_CpGs.tsv":
                        This file lists the CpGs that were used to calculate the
                        DNAm age. "<PREFIX>.missed_CpGs.txt": This file provides a
                        list of clock CpGs that were missed or excluded from the
                        input file. "<PREFIX>.coef.tsv": This file contains a list
                        of clock CpGs along with their coefficients. The last column
                        indicates whether the CpG is included in the calculation.
                        "<PREFIX>.plots.R": This file is an R script used to
                        generate visualization plots. "<PREFIX>.coef_plot.pdf": This
                        file is the coefficient plot in either PDF or PNG format.
  ...

Documentation
==============
`https://epical.readthedocs.io/en/latest/ <https://epical.readthedocs.io/en/latest/>`_
