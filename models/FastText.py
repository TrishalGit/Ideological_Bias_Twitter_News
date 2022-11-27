import fasttext
import os
import csv

directory = os.getcwd()

train_filenames = ['Left_Train', 'Right_Train', 'Neutral_Train']
test_filenames = ['Left_Test', 'Right_Test', 'Neutral_Test']

def get_accuracy(model, test_filename):
    correct_pred = 0
    total = 0
    with open(directory + '/Ideological_Bias_Twitter_News/data/train_test_split/' + test_filename + '.csv', 'r') as file:
        csvFile = csv.reader(file, delimiter=",")
        for lines in csvFile:
            total += 1
            predict = model.predict(lines[0].replace('\n', ' '))
            if lines[1].lower() in predict[0][0]:
                correct_pred += 1
                
    return (correct_pred / total) * 100

for i in range(len(train_filenames)):
    model = fasttext.train_supervised(input=train_filenames[i] + '.train', epoch = 1000)
    for j in range(len(test_filenames)):
        result = model.test(test_filenames[j] + '.test')
        F1Score = (2 * result[1] * result[2]) / (result[1] + result[2])
        accuracy = get_accuracy(model, test_filenames[j])
        
        print('FastText Accuracy Score for ' + train_filenames[i] + ' and ' + test_filenames[j] + ' -> ', accuracy)
        print('FastText F1 Score for ' + train_filenames[i] + ' and ' + test_filenames[j] + ' -> ', F1Score)
