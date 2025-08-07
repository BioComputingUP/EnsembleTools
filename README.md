# IDPEnsembleTools

<img src="https://raw.githubusercontent.com/BioComputingUP/EnsembleTools/main/images/idpet_logo_1.png" alt="IDPEnsembleTools Logo" width="180" height="70" />

[![PyPI](https://img.shields.io/pypi/v/idpet.svg)](https://pypi.org/project/idpet/)
<!-- [![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.1234567-blue)](https://doi.org/10.5281/zenodo.1234567) -->

---

## IDPEnsembleTools: An Open-Source Library for Analysis of Conformational Ensembles of Disordered Proteins

IDPEnsembleTools is a Python package designed to facilitate the **loading, analysis, and comparison** of multiple conformational ensembles of intrinsically disordered proteins (IDPs).

It supports various input formats such as `.pdb`, `.xtc`, and `.dcd`, and enables users to extract both **global** and **local** structural features, perform dimensionality reduction, and compute similarity scores between ensembles.

<img src="https://raw.githubusercontent.com/BioComputingUP/EnsembleTools/main/images/pipline_example.jpeg" alt="Pipeline Example" width="600" />

---

## Features

With **IDPEnsembleTools**, you can:

- **Extract global features** of structural ensembles:
  - Radius of gyration (Rg)
  - Asphericity
  - Prolateness
  - End-to-end distance

- **Extract local features**:
  - Interatomic distances
  - Phi–psi angles
  - Alpha-helix content

- **Perform dimensionality reduction** on ensemble features:
  - PCA
  - UMAP
  - t-SNE

- **Compare structural ensembles** using:
  - Jensen-Shannon (JS) divergence
  - Visualize similarity matrices

---

## Example Notebooks

The `notebooks/` directory contains a collection of Jupyter notebooks that demonstrate how to use the `EnsembleTools` package. These examples cover key functionalities such as ensemble comparison, dimensionality reduction (PCA, t-SNE, UMAP), feature extraction, and visualization customization. They serve both as tutorials and reproducible workflows for analyzing disordered protein ensembles.

| Notebook                      | Description                                                                                   | Link |
|------------------------------|-----------------------------------------------------------------------------------------------|------|
| `comparing_ensembles.ipynb`  | Compare multiple conformational ensembles using selected metrics and visualizations.          | [View](https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/comparing_ensembles.ipynb) |
| `featurization.ipynb`        | Generate numerical features from protein ensembles for downstream analysis.                   | [View](https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/featurization.ipynb) |
| `kpca_analysis.ipynb`        | Perform Kernel PCA to capture non-linear variance in ensemble structures.                     | [View](https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/kpca_analysis.ipynb) |
| `loading_data.ipynb`         | Load and preprocess ensemble data from various formats.                                       | [View](https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/loading_data.ipynb) |
| `pca_analysis.ipynb`         | Principal Component Analysis (PCA) for dimensionality reduction and visualization.            | [View](https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/pca_analysis.ipynb) |
| `plot_customization.ipynb`   | Customize plots for clarity and publication-quality visualizations.                           | [View](https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/plot_customization.ipynb) |
| `sh3_example.ipynb`          | Case study: global and local analysis of the SH3 domain of the Drk protein.                   | [View](https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/sh3_example.ipynb) |
| `tsne_analysis.ipynb`        | t-SNE embedding of ensemble features to explore local structure.                              | [View](https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/tsne_analysis.ipynb) |
| `umap_analysis.ipynb`        | UMAP embedding of ensemble features and visualization.                                | [View](https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/umap_analysis.ipynb) |


---
## Installation

It is recommended to install `idpet` in a **clean virtual environment** to avoid conflicts with existing packages.


### 🔹 Option 1: Using `conda` (if you use Anaconda/Miniconda)

```bash
# Create and activate a new conda environment
conda create -n idpet-env python=3.9
conda activate idpet-env

# Install the package from PyPI
pip install idpet
```


### 🔹 Option 2: Using `venv` (standard Python)

```bash
# Create a new virtual environment (Python 3.7+)
python -m venv idpet-env

# Activate the environment
# On Linux/macOS:
source idpet-env/bin/activate
# On Windows:
idpet-env\Scripts\activate

# Upgrade pip and install the package
pip install --upgrade pip
pip install idpet 
```

### Developer Installation (from source)
```bash
git clone https://github.com/BioComputingUP/EnsembleTools.git
cd idpet
pip install -e .
```

## License
This project is licensed under the [MIT License](LICENSE).
