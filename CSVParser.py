import json
import csv
import nltk
from collections import defaultdict
from nltk.stem import *

# Use defaultdict for comments so can append comments
comments = defaultdict(list)
categories = {}

def pDict(comments_location, articles_location):
    # Reads .csv file and imports it to dictionaries based on article id

    reader = csv.DictReader(open(comments_location, encoding='utf-8'))
    for row in reader:
        if row['commentBody'] == "":  # if empty, skip it
            continue
        else:
            #comments[row['articleID']] = row['commentBody']
            comments[row['articleID']].append(row['commentBody'])
    reader = csv.DictReader(open(articles_location, encoding='utf-8'))
    for row in reader:
        if row['articleID'] not in comments.keys():
            continue  # if skipped in comments, skip it also
        else:
            categories[row['articleID']] = row['keywords'] #jsons.load() wasn't needed here?


if __name__ == '__main__':

    pDict('nyt-comments/CommentsApril2017.csv','nyt-comments/ArticlesApril2017.csv' )
    pDict('nyt-comments/CommentsApril2018.csv','nyt-comments/ArticlesApril2018.csv' )


    with open('comments.json', 'w') as fp:
        fp.write(json.dumps(comments, indent = 4))

    with open('categories.json', 'w') as fp:
        fp.write(json.dumps(categories, indent = 4))


    # print(categories) # Test if worked
    # print(comments)

