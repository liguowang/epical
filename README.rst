|Documentation Status|

.. |Documentation Status| image:: https://readthedocs.org/projects/ansicolortags/badge/?version=latest
   :target: https://epical.readthedocs.io/?badge=latest

|Maintenance yes|

.. |Maintenance yes| image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity

|made-with-python|

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

|made-with-sphinx-doc|

.. |made-with-sphinx-doc| image:: https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg
   :target: https://www.sphinx-doc.org/

|PyPI format|

.. |PyPI format| image:: https://img.shields.io/pypi/format/ansicolortags.svg
   :target: https://pypi.org/project/epical/

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



Documentation
=============
`https://epical.readthedocs.io/en/latest/ <https://epical.readthedocs.io/en/latest/>`_
