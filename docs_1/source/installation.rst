Installation
============

We recommend installing IDPET in a clean virtual environment to avoid package conflicts. Below are step-by-step instructions for installation using either `venv` or `conda`, along with important setup notes for MDTraj.

Install using pip
-----------------

To install IDPET using pip, follow these steps:

Step 1: (Recommended) Create a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Using venv (standard Python):**

.. code-block:: bash

    python -m venv idpet-env

    # Activate the environment
    # On Linux/macOS:
    source idpet-env/bin/activate
    # On Windows:
    idpet-env\Scripts\activate

    # Upgrade pip
    pip install --upgrade pip

**Using conda:**

.. code-block:: bash

    conda create -n idpet-env python=3.9 -y
    conda activate idpet-env

Step 2: Install MDTraj (required)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IDPET is built on top of `MDTraj <https://mdtraj.org/>`_. Since MDTraj can have compatibility issues on Windows, we recommend installing it via `conda`:

.. code-block:: bash

    conda install -c conda-forge mdtraj

This step is **optional on Linux**, but still safe and recommended to avoid binary issues.

Step 3: Install IDPET
~~~~~~~~~~~~~~~~~~~~~

With your environment active and MDTraj installed, you can now install IDPET from PyPI:

.. code-block:: bash

    pip install idpet

To verify the installation:

.. code-block:: python

    import idpet
    print(idpet.__version__)

Developer installation (optional)
---------------------------------

If you wish to contribute to IDPET or work with the source code, you can install it in editable mode:

.. code-block:: bash

    git clone https://github.com/hamidrgh/idpet.git
    cd idpet
    pip install -e .

This will install IDPET in "editable" mode so any local changes take effect immediately.



