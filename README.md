# Discovering and Visualizing Research Topics
The goal of this project is to determine major research topics at UC Santa Barbara's Earth Research Institute (ERI) and visualize how they have changed over the last decade. To determine the major topics of research, we analyzed the publications and funded projects of ERI researchers from **2009 - 2019**. ERI maintains lists of active principal investigators (PIs). We used this list of active PIs to search for published articles using the Dimensions.ai API. The list of published articles we obtained were hand-curated by ERI administrative staff. ERI maintains funded project metadata internally. Only publications or funded projects with titles and abstracts were considered. This resulted in **publications (3,108)** and **funded projects (662)** that were combined into a single corpus of **documents (3,770)** for analysis.

## 1 - Data Preprocessing
Text cleaning involved: removing records with identical identifiers (DOIs), removing HTML tags, and reformatting ASCII extended characters. Analysis of the cleaned text showed: the shortest document (title, abstract) is 128 characters, the longest document is 7,083 characters, and the mean document length is 1,678 characters. Distribution of funded projects and publications showed: the greatest number of publications (431) from 2014; the greatest number of funded projects (78) beginning in 2012; and the greatest number of funded projects (107) ending in 2015.

## 2 - Natural Language Processing
To prepare the documents for topic modeling, we followed standard natural language processing steps to reformat them as a dictionary and a corpus (bag of words). Natural language processing involved: extension of stopword list to include frequent and generic terms ('data', 'study', 'project', 'research', 'collaborative'), tokenization and conversion to lowercase, construction of n-gram models to preserve contiguous sequences of words (bigrams, trigrams), and lemmatization to resolve words to their base forms. From this processed text, we created a dictionary (word id, word frequency) and a corpus (bag of words) to use in topic modeling.

## 3 - Topic Modeling
We experimented with three unsupervised approaches to develop coherent topic models. The results from each approach are reported as follows:

### Latent Dirichlet Allocation (LDA)
This implementation uses MALLET. A random seed (1) ensures reproducibility of model. Iterations through topics 2 - 100 determined the model with the best coherence score. The model with **47 topics** yielded the highest coherence score (0.5277) with the second and third highest scores from the models with 50 and 68 topics respectively. The hyperparameter for optimize interval was set to default after suboptimal results setting it to 10. 

The following summarize the results of the LDA 47 topic model: most representative document for each topic (LDA-47-rep-doc.csv); topic distribution across documents (LDA-47-top-dist.csv); and dominant topic for each document (LDA-47-top-doc.csv). The pyLDAvis (lda.html) supports model intepretation by showing salient terms from each of the topics in the model. 

### Non-negative Matrix Factorization (NMF)
This implementation uses scikit-learn. 

### hierarchical LDA (hLDA)
This implementation uses MALLET. 

## 4 - Spatialization and Visualization
###pyLDAVis of LDA

