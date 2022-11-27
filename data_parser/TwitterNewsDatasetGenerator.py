import snscrape.modules.twitter as sntwitter
import urllib.request as ur
import re
import csv
import os

directory = os.getcwd()
search_keyword = ['/politics/', '/world/']
categories = ['Politics', 'World']
news_media = ['FoxNews', 'CNN', 'NewsNation']
date_period = 'since:2015-12-01 until:2022-09-20'
tweet_count_per_topic = 740

def save_file(data, filename):
    file = open(directory + '/../data/' + filename + '.csv', 'w', newline='')
    writer = csv.writer(file, delimiter=",")
    writer.writerows(data)
    file.close()
    
    
for j in range(len(news_media)):
    count = [0] * len(categories)
    data = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:' + news_media[j] + ' ' + date_period).get_items()):
        text = tweet.content
        search_url = re.search("(?P<url>https?://[^\s]+)", text)
        category_id = -1
        url = ''
        new_article = False
        while search_url != None:
            tiny_url = search_url.group("url")
            try:
                if category_id == -1:
                    extract_url = ur.urlopen(tiny_url)
                    url = extract_url.geturl()
                    
                    # To make sure code is running
                    print(url)
                    
                    for k in range(len(categories)):
                        if search_keyword[k] in url and count[(k%2)] < tweet_count_per_category:
                            category_id = (k%2)
                            count[(k%2)] += 1
                            new_article = True
                            break
            except:
                # Do Nothing
            text = text.replace(tiny_url, '')
            search_url = re.search("(?P<url>https?://[^\s]+)", text)
            
        # To make sure code is running
        print(count[0], count[1])
        if category_id != -1:
            data.append([text, categories[category_id], url])
        if new_article and ((count[0] + count[1])%100) == 0:
            print('Saving File....')
            save_file(data, news_media[j])
        if count[0] >= tweet_count_per_topic and count[1] >= tweet_count_per_topic:
            break
    print('Saving File....')
    save_file(data, news_media[j])
