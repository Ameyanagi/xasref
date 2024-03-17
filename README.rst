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


.. code-block:: python

    import matplotlib.pyplot as plt
    from xasref import get_ref_dict


    ref = get_ref_dict()
    fe_k_group = ref["Fe K"]["group"]
    plt.plot(fe_k_group.energy, fe_k_group.mu)
    plt.show()

The dictionary that is returned by `get_ref_dict` contains the following keys.
You would probably need only `group`.

- `element`: The element name
- `group`: The reference data as a Larch group
- `edge`: The edge name
- `e0`: The e0 value
- `path`: The path to the reference data (source athena file)
- `label`: The label of the reference data (e.g. `Fe foil Fe K`)
- `dat_path`: The path to the reference data in a dat file

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

List of elements
----------------

- V K 5465eV
- Cr K 5989eV
- Mn K 6539eV
- Fe K 7112eV
- Co K 7709eV
- Ni K 8333eV
- Cu K 8979eV
- Zn K 9659eV
- Mo K 20000eV
- Ru K 22117eV
- Rh K 23220eV
- Pd K 24350eV
- Ag K 25514eV
- Cd K 26711eV
- In K 27940eV
- Sn K 29200eV
- W K 10207eV
- Re L3 10535eV
- Pt L3 11564eV
- Au L3 11919eV
- Zr K 17998eV

* Free software: MIT license
* Documentation: https://xasref.readthedocs.io.
