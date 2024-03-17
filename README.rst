======
xasref
======


.. image:: https://img.shields.io/pypi/v/xasref.svg
        :target: https://pypi.python.org/pypi/xasref

.. image:: https://img.shields.io/travis/Ameyanagi/xasref.svg
        :target: https://travis-ci.com/Ameyanagi/xasref

.. image:: https://readthedocs.org/projects/xasref/badge/?version=latest
        :target: https://xasref.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status



This repository contains a collection of XAS reference data recorded mainly in X18B beamline at NSLS and QAS beamline at NSLS-II.
Please feel free give a pull request to add any reference data.

The data other than the foil will also be added in the future.

Installation
------------

.. code-block:: bash
    pip install git+https://github.com/Ameyanagi/xasref


How to use
----------

The reference can be readily read by `get_ref_dict`. The following is an example to read Fe K reference data and plot it.

.. inculde:: ./examples/01_basic.py

How to generate the reference from the source and check the reference data
----------

The reference data is generated from the source file that is saved as a athena project file.
The files already converted to a dat file that have `energy, mu, and first derivative` columns.
Howevery, if you prefer to do this process by yourself, the following is the instruction.

The `g` or `--generate` option will generate the reference data from the source file and save it as a dat file.

.. code-block:: bash
    xasref -g

The `c` or `--check` option is use to check the quality of the reference dat file generated. The following is the example to check the reference data.
It will plot the reference data along with the first derivative, e0 and expected e0.
Please make sure that the data look reasonable to you.

.. code-block:: bash
    xasref -c


`-g` and `-c` can be used together as follows.

.. code-block:: bash
    xasref -g -c


* Free software: MIT license
* Documentation: https://xasref.readthedocs.io.
