

Badges which can be included! <br>
![PyPI](https://img.shields.io/pypi/v/IDPEnsembletools.svg)
![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.1234567-blue)


<img src="/images/idpet_logo_1.png" alt="Logo" width="180" height="70" />

# IDPEnsembleTools : an open-source library for analysis of conformational ensembles of disordered proteins 
![Pipline Example](/images/pipline_example.jpeg)

## Overview
IDPensembleTools is a python package by which you can load and analyze multiple conformational ensembles in different formats such as (`pdb`, `xtc`,`dcd`,...)

## Features 
With IDPensembleTools, you can:

- Extract and visualize **global features** of structural ensembles such as (`Rg`, `Asphericity`, `Prolateness`, `End to end distance`,...)
- Extract and visualize **local features** of structural ensembles sucha as ( `intera-atomic distances`, `phi-psi angles` , `alpha-helix content`, ...)
- Performing **dimensionality reduction** methods (`PCA`, `UMAP`, `t-SNE`) on different extracted features of structural ensemble
- **Comparing** structural ensembles of disordered proteins using different similarity scores such as Kullback-Leibler (KL) and Jensen-Shannon (JS) divergence methods and visualize similarity matrix
  
For details, you can check our user-centric documentation , **put the link to the documentation**, is generated from our repository using Sphinx. 

## Installation 
- Using pip:
Using python package managment systme "pip" you can easily install IDPensembleTools (and its dependencies if needed), upgrade or uninstall with just one terminal command. 

`pip install idpet`<br>
`pip install --upgrade idpet`<br>
`pip uninstall idpet`

- From source:
  
```bash
git clone https://github.com/hamidrgh/EnsembleTools.git
cd EnsembleTools
python setup.py install
```

## Python Requirements and Dependencies

- Recommend specific version of Python
- Point to the dependencies (Numpy, Sklearn, pandas, matplotlib, mdtraj, ...)

## Documentation
  
For details, you can check our user-centric [documentation](https://hamidrgh.github.io/gh_pages_idpet/overview.html), is generated from our repository using Sphinx. 

## Citation 
The link to the publication should be put here. 

## License
MIT License



