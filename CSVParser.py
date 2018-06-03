import json
import csv
import re
from collections import defaultdict


def pStopwords():
    with open('nltk.txt', 'r') as f:
        list = f.readlines()

    for i in range(len(list)):
        list[i] = list[i].replace('\n', '')

    return list

def pDict(comments_location, articles_location):
    comments = defaultdict(list)
    categories = {}
    # Reads .csv file and imports it to dictionaries based on article id
    count = 0
    reader = csv.DictReader(open(comments_location, encoding='utf-8'))
    for row in reader:
        if row['commentBody'] == "":  # if empty, skip it
            continue
        else:
            words = pfilter(row['commentBody'])
            #comments[row['articleID']] = row['commentBody']
            comments[row['articleID']].append(words)
            count += 1
            if count % 5000 == 0:
                print('Number of comments added to dictionary: ', count)
    reader = csv.DictReader(open(articles_location, encoding='utf-8'))
    count = 0
    for row in reader:
        if row['articleID'] not in comments.keys():
            continue  # if skipped in comments, skip it also
        else:
            categories[row['articleID']] = row['keywords'] #jsons.load() wasn't needed here?
            count += 1
            if count % 250 == 0:
                print('Number of categories added to dictionary: ', count)

    return comments, categories

def pfilter(string):
    # get rid of common unicode characters that aren't letters
    unicodes = ["<br/><br/>", "<br/>", '\"', "\u201c", "\u201d","\u2014","\u2015",
                "\u2015","\u2016","\u2017","\u2018","\u2019",]
    stopwords = pStopwords()
    filters = re.compile("[^A-Za-z0-9 ]+")
    string = re.sub(filters, "", string.lower())
    filtered_sentence = []
    for entry in unicodes:
        string = string.replace(entry, " ")
    tokens = string.split(' ')
    for word in tokens:
        if word not in stopwords and word != "":
            filtered_sentence.append(word)
    return filtered_sentence

if __name__ == '__main__':

    sComments = 'Comments'
    oCategories = 'categories'
    oComments = 'comments'
    sArticles = 'Articles'
    months = ['Jan', 'Feb','March', 'April', 'May'  ]
    years = ['2017', '2018']
    fileEnding = '.csv'
    jason = '.json'
    folder = 'nyt-comments/'

    for month in months:
        for year in years:
            # Use defaultdict for comments so can append comments
            cLocation =  folder + sComments + month + year + fileEnding
            aLocation =  folder + sArticles + month + year + fileEnding
            writeCmt = oComments + month + year + jason
            writeCat = oCategories + month + year + jason
            cmts, cats = pDict(cLocation, aLocation)
            with open(writeCmt, 'w') as fp:
                fp.write(json.dumps(cmts, indent = 4))
            with open(writeCat, 'w') as fp:
                fp.write(json.dumps(cats, indent = 4))

            print('Finished writing to json for ', month, ' ', year)

            # Testing automating file names
            # print(sComments + month + year + fileEnding)
            # print(sArticles + month + year + fileEnding)



