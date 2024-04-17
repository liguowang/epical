Installation
=============

*Epical* is coded in Python. It needs Python 3 (version >= 3.5.x  and <= 3.11.x) or a later
version for installation and execution.

Prerequisites
--------------

- `Python 3 <https://www.python.org/downloads/>`_ (>=3.5.x, <3.11.x)
- `pip3 <https://pip.pypa.io/en/stable/installing/>`_
- `R <https://www.r-project.org/>`_

Python Dependencies
--------------------

- `pandas <https://pandas.pydata.org/>`_
- `numpy <http://www.numpy.org/>`_
- `scipy <https://www.scipy.org/>`_
- `sklearn <https://www.scilearn.com/>`_
- `bx-python <https://github.com/bxlab/bx-python>`_
- `matplotlib <https://matplotlib.org/>`_
- `EpigeneticPacemaker <https://epigeneticpacemaker.readthedocs.io/en/latest/>`_
- `TensorFlow <https://www.tensorflow.org/>`_

.. note::
   As of Jan 10, 2024. TensorFlow does NOT support Python 3.12 and 3.13

.. note::
   Users do NOT need to install these packages manually, as they will be
   automatically installed if you use
   `pip3 <https://pip.pypa.io/en/stable/installing/>`_.


Install Epical
---------------

# Create virtual environment. In this example, we used `conda <https://docs.conda.io/en/latest/>`_ to create a virtual environment named *bioage*.

:code:`conda create -n bioage`
::
 
 Collecting package metadata (current_repodata.json): done
 Solving environment: done
 ...

# Activate the *bioage* virtual environment

:code:`conda activate bioage`

# Install *epical*

:code:`pip3 install epical`
::

 Collecting epical
   Downloading epical-0.0.1-py3-none-any.whl.metadata (2.4 kB)
 Requirement already satisfied: numpy in /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages (from epical) (1.26.3)
 Collecting scipy (from epical)
   Downloading scipy-1.11.4-cp311-cp311-macosx_10_9_x86_64.whl.metadata (60 kB)
      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.4/60.4 kB 923.3 kB/s eta 0:00:00
 Collecting scikit-learn (from epical)
   Downloading scikit_learn-1.3.2-cp311-cp311-macosx_10_9_x86_64.whl.metadata (11 kB)
 Collecting bx-python (from epical)
 ...


Upgrade *Epical*
-----------------

:code:`pip3 install epical --upgrade`

Uninstall *Epical*
-------------------

:code:`pip3 uninstall epical`
