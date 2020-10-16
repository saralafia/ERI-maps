## ERI-Maps
This repository contains notebooks and data for evaluating topic modeling approaches (LDA, hLDA, NMF) and mapping approaches (UMAP, t-SNE). The data in this analysis support an institutional review for the UC Santa Barbara Earth Research Institute [ERI](https://www.eri.ucsb.edu/). Administrative documents are found [here](https://adminweb.eri.ucsb.edu/Review/ReviewDocuments/). 

### Data

PI, projects, publications (2009 - 2014). Raw data and pre-processing steps are available in this [repo](https://github.com/saralafia/ERI-5-year-review).

### Notebooks

- Heuristics (**notebooks/ERI-heuristics.ipynb**) explores the data structure to approximate a suitable number of topics to model 
- LDA (**notebooks/ERI-LDA.ipynb**) pre-processes publication metadata (titles, abstracts), implements Latent dirichlet allocation, and calculates model coherence. It also generates a [pyLDAvis](pyLDavis.readthedocs.io) browser to explore the model.
- hLDA (**notebooks/ERI-LDA.ipynb**) implements hierarchical Latent dirichlet allocation, and calculates model perplexity using [Tomotopy](https://bab2min.github.io/tomotopy/v0.9.0/en/).
- NMF (**notebooks/ERI-LDA.ipynb**) creates a term frequency-inverse document frequency matrix of terms in the metdata for non-negative matrix factorization and calculates model coherence.
- ERI-maps (**notebooks/ERI-maps.ipynb**) clusters research documents using the outputs of the NMF topic model approach with t-SNE, UMAP, and word embedding.
- ERI-trees (**notebooks/ERI-trees.ipynb**) represents the relationship between topics at two levels of detail by clustering topics with a dendrogram.

### Mallet

[Mallet](http://mallet.cs.umass.edu/) is a package for topic modeling, used with a [Gensim](https://radimrehurek.com/gensim/models/wrappers/ldamallet.html) wrapper in the LDA notebook.

### Outputs
Files generated from running each of the models are stored here. These data are used to build the dashboard in this [repo](https://github.com/saralafia/ERI-dashboard).

### Figures

Examples of maps generated with t-SNE, UMAP, and word embedding at two levels of topics (9, 70). 

### License
[MIT](https://choosealicense.com/licenses/mit/)




