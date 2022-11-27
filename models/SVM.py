from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import os
import csv

directory = os.getcwd()

train_filenames = ['Left_Train', 'Right_Train', 'Neutral_Train']
test_filenames = ['Left_Test', 'Right_Test', 'Neutral_Test']

train_data = []
test_data = []
train_labels = []
test_labels = []

for i in range(len(train_filenames)):
    data = []
    labels = []
    with open(directory + '/Ideological_Bias_Twitter_News/data/train_test_split/' + train_filenames[i] + '.csv', 'r') as file:
        csvFile = csv.reader(file, delimiter=",")
        for lines in csvFile:
            data.append(lines[0])
            labels.append(lines[1])
            
    train_data.append(data)
    train_labels.append(labels)
    
    data = []
    labels = []
    with open(directory + '/Ideological_Bias_Twitter_News/data/train_test_split/' + test_filenames[i] + '.csv', 'r') as file:
        csvFile = csv.reader(file, delimiter=",")
        for lines in csvFile:
            data.append(lines[0])
            labels.append(lines[1])
            
    test_data.append(data)
    test_labels.append(labels)
    
for i in range(len(train_filenames)):
    text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', KNeighborsClassifier()),
                     ])

    text_clf.fit(train_data[i], train_labels[i])
    
    for j in range(len(test_filenames)):
        predicted = text_clf.predict(test_data[j])

        print('KNN Accuracy Score for ' + train_filenames[i] + ' and ' + test_filenames[j] + ' -> ',accuracy_score(predicted, test_labels[j])*100)
        print('KNN F1 Score for ' + train_filenames[i] + ' and ' + test_filenames[j] + ' -> ', f1_score(predicted, test_labels[j], pos_label="politics")*100)
