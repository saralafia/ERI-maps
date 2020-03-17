# Read Me
The goal of this project is to determine major research topics at UC Santa Barbara's Earth Research Institute (ERI) and visualize how they have changed over the last decade.

## Data Preprocessing
To determine the major topics of research, we analyzed the publications and funded projects of ERI researchers from **2009 - 2019**. ERI maintains lists of active principal investigators (PIs). We used this list of active PIs to search for published articles using the Dimensions.ai API. ERI maintains funded project metadata. This resulted in **publications (3,108)** and **funded projects (662)**. Only publications or funded projects with titles and abstracts were considered. Publications and funded projects were combined into a single corpus of **documents (3,770)**. 

Text cleaning involved: removing records with identical identifiers (DOIs), removing HTML tags, and reformatting ASCII extended characters. Analysis of the cleaned text showed: the shortest document (title, abstract) is 128 characters, the longest document is 7,083 characters, and the mean document length is 1,678 characters. Distribution of funded projects and publications showed: the greatest number of publications (431) from 2014; the greatest number of funded projects (78) beginning in 2012; and the greatest number of funded projects (107) ending in 2015.

## Natural Language Processing
To prepare the documents for topic modeling, we followed standard natural language processing steps to reformat them as a dictionary and a corpus (bag of words). 

Natural language processing involved: expansion of stopword list to include generic terms like "abstract", "background", "study", "data", "paper", "project", "review", "study" (for a complete list of stopwords, see /MALLET...)

## Topic Modeling

## Spatialization and Visualization

