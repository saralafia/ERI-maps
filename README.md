# Discovering and Visualizing Research Topics
The goal of this project is to determine major research topics at UC Santa Barbara's Earth Research Institute (ERI) and visualize how they have changed over the last decade. To determine the major topics of research, we analyzed the publications and funded projects of ERI researchers from **2009 - 2019**. ERI maintains lists of active principal investigators (PIs). We used this list of active PIs to search for published articles using the Dimensions.ai API. The list of published articles we obtained were hand-curated by ERI administrative staff. ERI maintains funded project metadata internally. Only publications or funded projects with titles and abstracts were considered. This resulted in **publications (3,108)** and **funded projects (662)** that were combined into a single corpus of **documents (3,770)** for analysis.

## 1 - Data Preprocessing
Text cleaning involved: removing records with identical identifiers (DOIs), removing HTML tags, and reformatting ASCII extended characters. Analysis of the cleaned text showed: the shortest document (title, abstract) is 128 characters, the longest document is 7,083 characters, and the mean document length is 1,678 characters. Distribution of funded projects and publications showed: the greatest number of publications (431) from 2014; the greatest number of funded projects (78) beginning in 2012; and the greatest number of funded projects (107) ending in 2015.

## 2 - Natural Language Processing
To prepare the documents for topic modeling, we followed standard natural language processing steps to reformat them as a dictionary and a corpus (bag of words). Natural language processing involved: extension of stopword list to include frequent and generic terms ('data', 'study', 'project', 'research', 'collaborative'), tokenization and conversion to lowercase, construction of n-gram models to preserve contiguous sequences of words (bigrams, trigrams), and lemmatization to resolve words to their base forms. From this processed text, we created a dictionary (word id, word frequency) and a corpus (bag of words) to use in topic modeling.

## 3 - Topic Modeling
We experimented with unsupervised approaches to develop coherent topic models. The results from each approach are reported as follows:

### Latent Dirichlet Allocation (LDA)
We experimented with two LDA implementations, summarized below. In each, the random seed or random state was set to 1 to ensure model reproducibility. Iterations through topics (2 - 100) determined a number of topics that yielded the best coherence score for each model. A pyLDAvis interface for each (lda-mallet-47.html, lda-mallet-20.html, lda-gensim-47.html, lda-gensim-14.html, lda-scikitlearn-10.html) supports intepretation by showing salient terms for each of the topics.

| Implementation | Topics| Coherence Score (0 - 1) |
|----------|-------------:|------:|
| MALLET LDA | 47 | 0.5277 |
| MALLET LDA | 20 | 0.5256 |
| Gensim LDA |    47   | 0.4499 | 
| Gensim LDA |    14   | 0.4802 | 
| Scikit-learn LDA |    10   | NA (log-likelihood = -667324.5189)| 

Overall, the MALLET LDA implementation produced higher quality topics. For the MALLET LDA topic model with the highest coherence score, we found: the most representative document for each topic (LDA-47-rep-doc.csv); the topic distribution across documents (LDA-47-top-dist.csv); and the dominant topic for each document (LDA-47-top-doc.csv). 

### Non-negative Matrix Factorization (NMF)
We experimented with an NMF implementation, summarized below.   

| Implementation | Topics| Coherence Score (0 - 1) |
|----------|-------------:|------:|
| Sci-kit learn NMF | |  |

### Hierarchical LDA (hLDA)
We experimented with an hLDA implementation, summarized below.   

| Implementation | Topics| Coherence Score (0 - 1) |
|----------|-------------:|------:|
| MALLET hLDA |      |  | 

### Other topic models and coherence scores:
* Latent Semantic Indexing (LSI): 5 topics (0.4470)
* Hierarchical Dirichlet Process (HDP): 20 topics (0.4948)

## 4 - Spatialization and Visualization
###LDA t-SNE

###hLDA hierarchical network