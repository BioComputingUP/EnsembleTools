.. functions analysis documentation master file, created by
   sphinx-quickstart on Tue May 21 12:57:48 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Demo
==============================================

We designed the IDPET Python package to facilitate the study and analysis of conformational ensembles of intrinsically disordered proteins. These proteins, known for their dynamic and highly variable structures, play a fundamental role in various biological processes.

Here, we highlight four different types of analyses that can be performed using IDPET. For more details you can also check the jupyter notebooks provided in the github repository.  

.. rubric:: Notebooks Overview


Here’s a summary of the example notebooks available in the github repository:

.. grid:: 1 1 2 3
   :gutter: 2

   .. card:: ``comparing_ensembles``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/comparing_ensembles.ipynb
      :link-type: url

      Compare multiple conformational ensembles using selected metrics and visualizations.

   .. card:: ``featurization``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/featurization.ipynb
      :link-type: url

      Generate numerical features from protein ensembles for downstream analysis.

   .. card:: ``kpca_analysis``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/kpca_analysis.ipynb
      :link-type: url

      Perform Kernel PCA to capture non-linear variance in ensemble structures.

   .. card:: ``loading_data``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/loading_data.ipynb
      :link-type: url

      Load and preprocess ensemble data from various formats.

   .. card:: ``pca_analysis``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/pca_analysis.ipynb
      :link-type: url

      Principal Component Analysis (PCA) for dimensionality reduction and visualization.

   .. card:: ``plot_customization``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/plot_customization.ipynb
      :link-type: url

      Customize plots for clarity and publication-quality visualizations.

   .. card:: ``sh3_example``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/sh3_example.ipynb
      :link-type: url

      Case study: global and local analysis of the SH3 domain of the Drkn protein.

   .. card:: ``tsne_analysis``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/tsne_analysis.ipynb
      :link-type: url

      t-SNE embedding of ensemble features to explore local structure.

   .. card:: ``umap_analysis``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/umap_analysis.ipynb
      :link-type: url

      UMAP embedding for global manifold learning and visualization.

   .. card:: ``idpet_vs_soursop``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/idpet_vs_soursop.ipynb
      :link-type: url

      A comparative analysis between IDPET and Soursop packages for ensemble analysis.

   .. card:: ``MDP``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/MDP.ipynb
      :link-type: url

      Example to perform analysis for Multi Domain Proteins.

   .. card:: ``alpha_synuclein``
      :link: https://github.com/BioComputingUP/EnsembleTools/blob/main/notebooks/alpha_synuclein.ipynb
      :link-type: url

      Analyze the structural features and dynamics of 5 different ensembles of the alpha-synuclein protein.

.. raw:: html

   <script type="text/javascript">
     function redirectToPage(url) {
      window.location.href = url;
     }
   </script>

   <style>
   .icons-container {
    display: flex;
    justify-content: space-between; /* Ordina verticalmente i contenitori delle icone */
    flex-wrap: center; /* Centra i contenitori delle icone horizontalmente */
    padding: 20px; /* Aggiunge uno spazio tra i contenitori delle icone */
   }

   .icon-item {
    text-align: center; /* Centra il testo all'interno del contenitore */
    margin-bottom:20px;
   }

   .icon-item img {
   cursor: pointer; /* Cambia il cursore in un puntatore quando si passa sopra le icone */
   width: 200px; /* Imposta la larghezza delle icone */
   height: 200px; /* Mantieni la proporzione delle icone */
   }

   .icon-item div {
   font-size: 12px; /* Imposta la dimensione del testo */
   color: #001; /* Imposta il colore del testo */
   }
   </style>


   <div class='icons-container'>
    <div class='icon-item'>
     <img src="_static/images/icons/gl_an.png" alt="global analysis" title="The global analysis of a protein's structure focuses on studying its total three-dimensional shape, aiming to understand how proteins fold and group together to form stable and functional structures." onclick="redirectToPage('Global_analysis.html')" style="cursor: pointer;width: 200px; height: 200px;">
     <div style="font-size: 12px; color: #001;">Global analysis</div>
    </div>

   <div class='icon-item'>
    <img src="_static/images/icons/l_an.png" alt="local analysis" title="The local analysis of a protein's structure focuses on examining specific regions, concentrating on secondary structural elements, with the aim of understanding folding patterns and interactions within those localized areas." onclick="redirectToPage('local_analysis.html')" style="cursor: pointer;width: 200px; height: 200px;">
    <div style="font-size: 12px; color: #001;">Local analysis</div>
   </div>

   <div class='icon-item'>
    <img src="_static/images/icons/tsne.png" alt="dimensional_reduction" title="Dimensionality reduction analysis focuses on simplifying complex data by reducing the number of independent variables needed to describe a system." onclick="redirectToPage('dimensional_reduction.html')" style="cursor: pointer;width: 200px; height: 200px;">
    <div style="font-size: 12px; color: #001;">Dimensionality Reduction analysis</div>
   </div>

   <div class='icon-item'>
    <img src="_static/images/icons/comp_ensambles.png" alt="comparing_ensamble" title="We have explored techniques for comparing and analyzing datasets, focusing on the calculation of various metrics " onclick="redirectToPage('comparing_ensambles.html')" style="cursor: pointer;width: 200px; height: 200px;">
    <div style="font-size: 12px; color: #001;">Ensemble Comparison</div>
   </div>

.. toctree::
   :hidden:

   Global_analysis

   local_analysis

   dimensional_reduction

   comparing_ensambles

