import urllib.request as ul
import re
import csv
import os
import json
import operator

directory = os.getcwd()

file = open(directory + '/NewsDataset/HarvardNewsTweets/dataverse_files/articles.json')
data = json.load(file)
file.close()

# Sort number of articles based on source url (news media)
articles_count = {}
for i in range(len(data)):
    source = data[i]['source']
    if source in articles_count.keys():
        articles_count[source] += 1
    else:
        articles_count[source] = 1
articles_count = sorted(articles_count.items(), key=operator.itemgetter(1))
print(articles_count)

# Get min count of articles for topics choosen
news_media = ['www.wsj.com', 'www.cnn.com', 'www.foxnews.com']
news_category_dist = [{}, {}, {}]
for i in range(len(data)):
    source = data[i]['source']
    category = data[i]['category_aggregate']
    for j in range(len(news_media)):
        if news_media[j] in source:
            if category in news_category_dist[j]:
                news_category_dist[j][category] += 1
            else:
                news_category_dist[j][category] = 1

categories = ['politics', 'world']
articles_per_category = 5000
for i in range(len(news_media)):
    for j in range(len(categories)):
        articles_per_category = min(articles_per_category, news_category_dist[i][categories[j]])

def save_file(data, filename):
    file = open(directory + '/NewsDataset/' + filename + '.csv', 'w', newline='')
    writer = csv.writer(file, delimiter=",")
    writer.writerows(data)
    file.close()

filenames = ['WSJHarvard', 'CNNHarvard', 'FoxNewsHarvard']
dataset = [[], [], []]
article_count = []
for i in range(len(news_media)):
    article_count.append({})
    for j in range(len(categories)):
        article_count[i][categories[j]] = 0

for i in range(len(data)):
    source = data[i]['source']
    category = data[i]['category_aggregate']
    text = data[i]['text']
    for j in range(len(news_media)):
        if news_media[j] in source:
            if category in categories and article_count[j][category] < articles_per_category:
                dataset[j].append([text, category])
                article_count[j][category] += 1
                
save_file(dataset[0], filenames[0])
save_file(dataset[1], filenames[1])
save_file(dataset[2], filenames[2])
