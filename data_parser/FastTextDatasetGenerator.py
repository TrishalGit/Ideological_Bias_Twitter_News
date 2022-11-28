import os
import csv

directory = os.getcwd()

#train_filenames = ['Left_Train', 'Right_Train', 'Neutral_Train']
#test_filenames = ['Left_Test', 'Right_Test', 'Neutral_Test']

# Comment the above lines and uncomment the below to run code on Harvard Dataset
train_filenames = ['Left_Harvard_Train', 'Right_Harvard_Train', 'Neutral_Harvard_Train']
test_filenames = ['Left_Harvard_Test', 'Right_Harvard_Test', 'Neutral_Harvard_Test']


def save_file(data, filename):
    file = open(directory + '/../data/fasttext/' + filename, 'w')
    file.writelines(data)
    file.close()

for i in range(len(train_filenames)):
    data = []
    with open(directory + '/../data/train_test_split/' + train_filenames[i] + '.csv', 'r') as file:
        csvFile = csv.reader(file, delimiter=",")
        for lines in csvFile:
            data.append('__label__' + lines[1].lower() + ' ' + lines[0] + '\n')
            
    save_file(data, train_filenames[i] + '.train')
    
for i in range(len(test_filenames)):
    data = []
    with open(directory + '/../data/train_test_split/' + test_filenames[i] + '.csv', 'r') as file:
        csvFile = csv.reader(file, delimiter=",")
        for lines in csvFile:
            data.append('__label__' + lines[1].lower() + ' ' + lines[0] + '\n')
            
    save_file(data, test_filenames[i] + '.test')
