# Designing Multi-Level Spatial Views of Research Themes
In this project, we determine major research themes at UC Santa Barbara's Earth Research Institute ([ERI](https://www.eri.ucsb.edu/)) and visualize their evolution over the last decade. Our goal is to complement quantitative, scientometric approaches for reviewing a body of research with qualitative, systematic approaches. We first create abstractions of the body of research with topic modeling and then use the topic models to map the body of research. The maps that we design show spatial views of ERI's research at multiple levels of thematic granularity, which support the academic review process. 

## Data sources and heuristics
We analyze funded projects and publications from ERI's **240** principal investigators (PIs) active from **2009 - 2019**. ERI maintains records of active PIs and funded projects. We gather PI publication metadata from the [Dimensions API](https://www.dimensions.ai/). Only funded projects or publications with titles and abstracts are analyzed, resulting in **3,770** research documents (3,108 publications and 662 funded projects). 

To determine a suitable range of topics to model, we first survey ERI's: 1) fields of research (from publications); 2) funding agencies (of projects); and 3) academic departments (of affiliated PIs). These heuristics do not capture the "aboutness" of ERI's research in terms of subjects or methods; thus they do not help to approximate a range of topics to model. However, these measures do highlight the multidisciplinarity of ERI's research portfolio and give a sense of its underlying shape.

- *Fields of research (FOR)*: University administrators or external funding agencies are often concerned with how research units are relatively positioned or compare externally across universities. Classification systems like FOR enable the comparison of research across academic divisions. Publications are classified hierarchically into [fields of research](https://dimensions.freshdesk.com/support/solutions/articles/23000018826-what-is-the-background-behind-the-fields-of-research-for-classification-system-) representing 22 divisions (broad subject areas or research disciplines) and 157 groups (detailed subsets of divisions). The publication database assigns FOR codes at the level of the individual article. Publications authored by ERI PIs represent **19 divisions**  and **112 groups** of academic research. The majority of ERI's research falls into just 4 divisions (summarized below). 

<div style="text-align:center"><img src="figures/FOR_divisions.png" alt="FOR_divisions" width="600"/></div>

- *Funding agencies*: ERI projects have received $191,235,929 over the past decade from **145 funding agencies**. Funders are classified into **5 categories**: Federal agencies; institutes of higher education; private agencies and foundations; California state and municipal agencies; and UC-wide funding. Funding agencies do not clearly signal an appropriate range of topics, but they do offer insights into the type of research being done (e.g. basic, applied). The 20 agencies that have funded the greatest number of ERI projects (summarized below) represent a mixture of sources. 

<div style="text-align:center"><img src="figures/top_20_funders.png" alt="project_funding" width="600"/></div>

- *Academic departments*: Over the last decade, ERI's 240 PIs have been affiliated with **24 academic departments**. Some affiliations have also changed (e.g. Crustal Studies has merged into other academic departments). Many PIs are solely affiliated with ERI, while others are secondarily affiliated (summarized below). Department affiliation is likely the weakest proxy for research topics since researchers from many disciplines may study similar subjects or use similar methods; the department of statistics for example is conspicuously absent despite the importance of statistical techniques across ERI's research.

<div style="text-align:center"><img src="figures/PI_depts.png" alt="project_funding" width="500"/></div>

Alternatively, cognitive heuristics capture "meaningful units" of information (levels of thematic granularity) that a viewer such as an external reviewer may have in mind. These heuristics seem to be better suited to our task of defining and designing a suitable range of topics to model.

- *Miller's law*: The average person can hold approximately 7±2 "chunks" in working memory (e.g. 7 digits, 6 letters, 5 words), limiting the transmission and processing of information (Miller, 1956). This suggests at least two levels of granularity for our topic models, with the coarsest granularity level of 7±2 (**5 - 9 chunks)** and the second level bounded by (5 x 5) to (9 x 9), a range of (**25 - 81 chunks**). 

## Natural Language Processing
We prepare the documents (titles and abstracts) for topic modeling by removing records with identical identifiers (DOIs), removing HTML tags, and reformatting ASCII extended characters. Documents range in length from 128 - 7,083 characters; the mean document length is 1,678 characters.

<div style="text-align:center"><img src="figures/word-count-dist.png" alt="project_funding" width="600"/></div>

We determine distinct document terms using the measure of term frequency–inverse document frequency (Salton et al., 1975). From these frequent terms, we select generic terms that qualify as stopwords and strip them from the documents. The 20 most distinctive (and possibly important) words in the documents, along with their relative weights, are:

1. data (72.55)
2. water (68.59)
3. species (67.42)
4. climate (64.61)
5. model (59.18)
6. soil (54.52)
7. snow (48.71)
8. change (47.67)
9. high (44.43)
10. surface (44.21)
11. based (42.98)
12. models (41.48)
13. ocean (38.30)
14. carbon (38.21)
15. spatial (37.74)
16. land (37.37)
17. results (36.83)
18. global (36.81)
19. california (36.53)
20. environmental (36.39)

Next, we follow a standard natural language processing pipeline (Boyd-Graber et al., 2014) to reformat the documents into a dictionary and a corpus: 

1. extension of the stopword list to remove frequent, generic terms determined by tf-idf ('data', 'study', 'project', 'research', 'collaborative', 'include', 'result', 'increase', 'high', 'low', 'large', 'include', 'based');
2. tokenization, conversion to lowercase, and construction of n-gram models (bigrams, trigrams) to preserve contiguous sequences of words (e.g. 'climate_change'); 
3. and lemmatization to resolve words to their base forms (e.g. 'specie') 

From the processed documents, we create a dictionary (of word ids, word frequencies) and a corpus (a bag of words shown as a wordcloud below) to use in topic modeling.

<div style="text-align:center"><img src="figures/wordcloud-cleaned-corpus.png" alt="project_funding" width="600"/></div> 

## Topic Modeling
Our goal in topic modeling is to reveal research topics unbounded by traditional silos (e.g. fields of research, funding agencies, academic departments). We experiment with several unsupervised approaches to develop coherent topic models. We consider the most important parameter of each model to be its *number of topics*. In addition to model coherence scores or measures of perplexity, we also consider the previously reported heuristics to determine a range of topic numbers to test. 

We take two kinds of topic modeling approaches: *probabilistic* (LDA, hLDA) and *matrix factorization* (NMF). In probabilistic approaches, each document is treated as a mixture of a small number of topics; words and documents get a probability score for each topic (Blei, 2003). In matrix factorization approaches, methods from linear algebra are applied to decompose a document-term matrix (tf-idf) into a smaller set of matrices, which can be interpreted as a topic model (Lee and Seung, 1999). 

In addition to the scientometric and cognitive heuristics we previously developed, we also report *coherence scores* for the topic models, which allow model comparison and evaluation across levels of thematic granularity. Coherence measures the extent to which top terms representing a topic are semantically related relative to the corpus (Mimno et al., 2011). This measure allows us to select a model with a number of topics yielding a relatively high coherence score. Compared with similar measures, including perplexity and log-likelihood, for evaluating topic model quality, coherence is considered to be more human interpretable (Greene et al., 2014). 

### Latent Dirichlet Allocation (LDA)
The LDA algorithm (Blei et al., 2003) is a generative probabilistic model. In each run of LDA, we set the random seed to 1, ensuring model reproducibility. The [MALLET](http://mallet.cs.umass.edu./) implementation of LDA produced higher quality topics than the Gensim and Scikit-learn implementations. We tested 2 - 100 topics based on the previously established heuristics and iterated through these to determine models yielding the highest coherence scores.

Following our heuristics, the model with the highest coherence score in the first level of thematic granularity (between 5 - 9 topics) has **8 topics** and the model with the highest coherence score in the second level (between 25 - 81 topics) has **43 topics**. The findings are summarized below.

<img src="figures/LDA-coherence-V2.png" alt="LDA-coherence" width="500"/>

| Number of Topics| Coherence Score (0 - 1) | 
|-------------:|-------------:|
| **43** | **0.5444**  |
| 47 |0.5376 | 
| 55 |0.5347  | 
| 67 |0.5330 | 
| 52 |0.5328 | 
| **8** | **0.4657** | 
| 9|0.462| 
| 7 |0.4576 | 
| 5|0.4317  | 
| 6|0.4292 | 

Wordclouds summarizing the first 10 topics of the model and the top 10 keywords for both models are shown below. Keywords are weighted within the topic and sized accordingly in each topic's wordcloud.

*8 topic wordcloud:*

<div style="text-align:center"><img src="figures/LDA-mallet-8-word-clouds.png" alt="project_funding" width="800"/></div>

*43 topic wordcloud:*

<div style="text-align:center"><img src="figures/LDA-mallet-43-word-clouds.png" alt="project_funding" width="800"/></div>

We produce interfaces to the topic models using [pyLDAvis](https://nbviewer.jupyter.org/github/bmabey/pyLDAvis/blob/master/notebooks/pyLDAvis_overview.ipynb). The browser-based tool offers an interactive visualization of topics estimated with LDA. The distance between topics (Jensen-Shannon divergence) is computed; multidimensional scaling (principal components) projects the intertopic distances onto two dimensions. The size of topics and their distributions, as well as the saliency of terms within each topic and across the entire corpus, are visible. As a result, pyLDAvis supports interpretation of the meaning of each topic; the prevalence of each topic; and the relationships among topics. 

*8 topic pyLDAvis:*

<img src="figures/pyLDAvis-8-topics.png" alt="LDA-coherence" width="600"/>

*43 topic pyLDAvis:*

<img src="figures/pyLDAvis-43-topics.png" alt="LDA-coherence" width="600"/>

The topics resulting from LDA largely suggest methods (e.g. "model", "analysis", "task") that are indicative of ERI's research. While this is an interesting result, we hope to use topic modeling to identify subject matter. For example, if oceanographic modeling is one of ERI's major research themes, we would hope for terms related to "ocean" to surface as a primary facet of the data rather than terms related to "modeling" (which would serve nicely as a secondary facet). While we can imagine organizing working groups or committees within ERI decicated to these shared methods, they are not the focus of our current work; they do not help us capture the "aboutness" of ERI's body of research. Next, we test an extension of LDA (hierarchical LDA) and an alternative, deterministic approach (NMF) to compare with our results from LDA.

### Hierarchical LDA (hLDA)

An extension of LDA for learning topic hierarchies is hLDA (Griffiths et al., 2004). This approach estimates the structure of a hierarchy and partitions documents nonparametrically. We implement hLDA with [Tomotopy](https://bab2min.github.io/tomotopy). The following summarizes our findings at several hierarchical levels. The hierarchical model with a depth of 4 has the lowest perplexity score, which measures how well a probability model predicts a sample for a given number of topics. 

The model producing the lowest perplexity score is the **4-level** hierarchical model. The first level for all models has 1 parent topic. Interpreting the number of topics using our heuristics, the second level of the 4-level model has **29 topics**, which is within the suitable range of topics that we predicted (25 - 81). Extending Miller's Law to a third and fourth level, a suitable range of topics for each would fall between ((5 x 5 x 5) to (9 x 9 x 9)) and ((5 x 5 x 5 x 5) to (9 x 9 x 9 x 9)) respectively. Neither the third nor fourth levels however fall within these wide predicted ranges; **83 topics** (125 - 729) and **409 topics** (625 - 6561). The findings from hierarchical models between 3 - 9 levels of depth are summarized below.

| Depth | Total Topics | Number of Topics per Level| Perplexity Score |
|----------|-------------:|------:|------:|
| 3|  393 | 1, 80, 312    | 3921.60 | 
| **4**|  **522** | **1, 29, 83, 409**     | **3622.80** | 
| 5|  555 | 1, 15, 39, 97, 403     | 3645.70 | 
| 6|  742 | 1, 17, 31, 69, 167, 457     | 3697.96 | 
| 7|  662 | 1, 8, 15, 32, 55, 134, 417    | 3928.90 | 
| 8|  807 | 1, 4, 12, 21, 39, 77, 166, 487    | 3867.75 | 
| 9|  1077 | 1, 5, 9, 11, 32, 77, 121, 243, 578   | 3996.23 | 

An example of topics taken from each of the 4-levels is shown below. Each topic is shown as a node labeled with its top 10 keywords; the edges connect parent topics (top) to children topics (below) and are weighted by the number of documents assigned to each topic. 

<img src="figures/hLDA-4-level.png" alt="LDA-coherence" width="600"/>

We expect that the topics we generate will emphasize similarities in the documents and that as a result, the topics will be well-distributed across the documents in the corpus; however, hLDA unevenly partitions the corpus with the majority of topics falling into broad, generic categories at each level. This method does not generate a relatively even distribution of topics to describe ERI's research; instead, it appears to emphasize work that is exceptionally different by distinguishing it into separate, comparatively small categories. For example, in the 4-level model, although there are 29 topics at the second level, most documents (3,586/3,770) fall into Topic 8; others, like Topic 10, are far more narrow and only describe a fraction of the documents (11/3,770). Furthermore, each level of the hierarchy appears to produce topics that are not comparably granular; Topic 10 in the 4-level model, for instance, is comprised of far more specific keywords than its second level counterparts. For these reasons, we decide not to pursue the hLDA topic model, although it may prove to be a useful technique for a more narrowly defined field of research.

### Non-negative Matrix Factorization (NMF)
The NMF approach (Arora et al., 2013) has been shown to produce higher quality topics for smaller or sparser datasets. We generate the NMF models using [Scikit-learn](https://scikit-learn.org/stable/) and use an initialization procedure called Nonnegative Double Singular Value Decomposition (nndsvd), which is appropriate for sparse data (e.g. document titles, abstracts only). We fit the models using the tf-idf features that we previously calculated. We test the same range of topics (2 - 100) as we did previously to determine models yielding the highest coherence scores; NMF produces models with higher coherence scores than the LDA models. 

Following our heuristics, the model with the highest coherence score in the first level of thematic granularity (between 5 - 9 topics) has **9 topics** and the model with the highest coherence score in the second level (between 25 - 81 topics) has **70 topics**. The findings are summarized below. 

<img src="figures/NMF-coherence.png" alt="LDA-coherence" width="500"/>

| Number of Topics| Coherence Score (0 - 1) |
|-------------:|------:|
| **70** | **0.7077** |
| 71 | 0.7063 |
| 74 | 0.7069 |
| 80 | 0.705 |
| 82 | 0.7064 |
| **9** | **0.5966** |
| 8 | 0.5828 |
| 7 | 0.5576 |
| 6 | 0.5200 |
| 5 | 0.5009 |

Of the three approaches to topic modeling, **NMF** appears to be the most promising for several reasons. Compared with the topics resulting from LDA, NMF produces topics that are more indicative of subject matter (rather than methods). The coherence scores of the NMF models are also higher than those of the LDA models and the NMF model is also better, making it suitable for dynamic topic modeling as the corpus is updated in the future.  

We adopt the NMF topic modeling approach at two-levels of thematic granularity: **a first level (5-9 topics)** and **a second level (25-81 topics)**. Our approach allows us to dynamically produce and or/update topic models with any number of topics within each of these ranges. We keep these levels of thematic granularity in mind as we spatialize the NMF topic model as they inform usability constraints (e.g. the number of chunks of information that reviewers are able to keep in mind). 

[Can NMF be used to build a text classifier for documents? Is this possible? What happens to the current topics if more documents are added to the corpus over time?]

## Spatialization

The topic models yield three main units around which the spatializations can be oriented: topics, documents, and keywords. Document authorship (for publications and grant proposals) allows us to also associate PIs with topics. While there are many possible configurations resulting from these units, our primary goal is to address the following questions:

1. How have ERI’s research **topics** changed?
2. Which ERI research **documents** (publications, projects) are similar?
3. Which of ERI **keywords** research shared topics?

These questions suggest distinct views of ERI's body of research. Using the most coherent topic models we selected at each level of thematic granularity, we develop spatial views of ERI's body of research. We structure these views along the lines of Franco Moretti's (2007) abstract models for literary history, which support "distant reading" of the corpus in the form of:

- **Graphs:** objects, event (time) topics changing over time
- **Maps:** objects, neighborhood (space); document clustering
- **Trees:** objects, network (combination of both); Topic/keyword relationships

We develop a prototype dashboard with [Plotly Dash](https://plotly.com/python/)... 

## References

Arora, S., Ge, R., Halpern, Y., Mimno, D., Moitra, A., Sontag, D., ... and Zhu, M. (2013). A practical algorithm for topic modeling with provable guarantees. In International Conference on Machine Learning (pp. 280-288).

Blei, D. M., Ng, A. Y., and Jordan, M. I. (2003). Latent dirichlet allocation. Journal of machine Learning research, 3(Jan), 993-1022.

Boyd-Graber, J., Mimno, D., & Newman, D. (2014). Care and feeding of topic models: Problems, diagnostics, and improvements. Handbook of mixed membership models and their applications, 225255.

Greene, D., O’Callaghan, D., & Cunningham, P. (2014). How many topics? stability analysis for topic models. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases (pp. 498-513). Springer, Berlin, Heidelberg.

Griffiths, T. L., Jordan, M. I., Tenenbaum, J. B., and Blei, D. M. (2004). Hierarchical topic models and the nested chinese restaurant process. In Advances in neural information processing systems (pp. 17-24).

Maaten, L. van der, and Hinton, G. (2008). Visualizing data using t-SNE. Journal of Machine Learning Research, 9(Nov), 2579–2605.

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological review, 63(2), 81.

Mimno, D., Wallach, H. M., Talley, E., Leenders, M., & McCallum, A. (2011, July). Optimizing semantic coherence in topic models. In Proceedings of the conference on empirical methods in natural language processing (pp. 262-272). Association for Computational Linguistics.

Salton, G., Wong, A., & Yang, C. S. (1975). A vector space model for automatic indexing. Communications of the ACM, 18(11), 613-620.