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

 # Create a  virtual environment ...

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
============


Print out usage and all the `available clocks <https://epical.readthedocs.io/en/latest/overview.html#available-clocks>`_
-------------------------------------------------------------------------------------------------------------------------

::

 $ epical --help
  usage: epical [-h] [-v] 
  {Horvath13, Horvath13_shrunk, Horvath18, Levine, ...}
  ...

Example: run the "Horvath13" command
-------------------------------------

::
 
 # print usage of the "Horvath13" command
 $ epical Horvath13 --help
 ...
 
 # run example data
 $ epical Horvath13 -m blood_N20_info.tsv -o output blood_N20_MethylationEPIC-v1.0_beta.tsv.gz
 2024-01-04 07:52:11 [INFO]  The prefix of output files is set to "output".
 2024-01-04 07:52:11 [INFO]  Loading Horvath13 clock data ...
 2024-01-04 07:52:11 [INFO]  Clock's name: "Horvath13"
 2024-01-04 07:52:11 [INFO]  Clock was trained from: "Pan-tissue"
 2024-01-04 07:52:11 [INFO]  Clock's unit: "years"
 2024-01-04 07:52:11 [INFO]  Number of CpGs used: 353
 ...

Documentation
==============
`https://epical.readthedocs.io/en/latest/ <https://epical.readthedocs.io/en/latest/>`_
