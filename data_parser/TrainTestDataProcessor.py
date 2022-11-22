import csv
import os
import random

directory = os.getcwd()

harvard_filenames = ['CNNHarvard', 'FoxNewsHarvard', 'WSJHarvard']
twitter_filenames = ['CNN', 'FoxNews', 'NewsNation']
output_file_substring = ['Left', 'Right', 'Neutral']

def save_file(data, filename):
    file = open(directory + '/../data/train_test_split/' + filename + '.csv', 'w', newline='')
    writer = csv.writer(file, delimiter=",")
    writer.writerows(data)
    file.close()

def build_train_test_split(filename, output_file_prefix):
    data = []
    with open(directory + '/../data/pre_processed/' + filename + '.csv', 'r') as file:
        csvFile = csv.reader(file, delimiter=",")
        
        for lines in csvFile:
            data.append([lines[0], lines[1].lower()])
    
    rec_numbers = [[], []]
    for i in range(len(data)):
        if data[i][1] == 'politics':
            rec_numbers[0].append(i)
        else:
            rec_numbers[1].append(i)
    
    test_article_count = 240
    politics_rec_numbers = random.sample(rec_numbers[0], test_article_count)
    world_rec_numbers = random.sample(rec_numbers[1], test_article_count)
    
    train_data = []
    test_data = []
    for i in range(len(data)):
        if i in politics_rec_numbers or i in world_rec_numbers:
            test_data.append(data[i])
        else:
            train_data.append(data[i])
            
    save_file(train_data, output_file_prefix + 'Train')
    save_file(test_data, output_file_prefix + 'Test')

for i in range(len(harvard_filenames)):
    build_train_test_split(harvard_filenames[i], output_file_substring[i] + '_Harvard_')

for i in range(len(twitter_filenames)):
    build_train_test_split(twitter_filenames[i], output_file_substring[i] + '_')
