# NYT-Comment-Preprocess
Python Implementation to preprocess NYT comments from .csv to .json

# Overview

This python script takes the .csv files from the New York Times Comments dataset found on kaggle and takes only 
the article keywords sorted by articleID and article comments sorted by articleID and exports those as dictionaries into 
separate .JSON files.  The comments are preprocessed to remove uppercase, punctuation, and stopwords based on the nltk stopwords.


# Requirements
	- Python 3.6.5 and default libraries csv, json, re, defaultdict from collections
	- nltk.txt 
	- The Kaggle dataset "Comments on articles published in the New York Times":  https://www.kaggle.com/aashita/nyt-comments
		- extracted to external folder in directory as "nyt-comments"