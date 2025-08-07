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

## 🔧 Features

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

## 📦 Installation

### Using `pip`

Install the latest release from PyPI:

```bash
pip install idpet
```
## 📄 License

This project is licensed under the [MIT License](LICENSE).
