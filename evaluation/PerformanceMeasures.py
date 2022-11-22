import csv
import os
import re

directory = os.getcwd()

# Add file paths to calculate performance measures
predictions = ['']
labels = ['']

def get_labels(filepath):
    label_list = []
    with open(directory + '/../data/' + filepath + '.csv', 'r') as file:
        csvFile = csv.reader(file, delimiter=",")
        for lines in csvFile:
            label_list.append(lines[1])
    return label_list

def calculate_performance(prediction_file, label_file):
    predict_labels = get_labels('predictions/' + prediction_file)
    actual_labels = get_labels('train_test_split/' + label_file)
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(len(predict_labels)):
        if predict_labels[i] == actual_labels[i]:
            if predict_labels[i] == 'politics':
                TP += 1
            else:
                TN += 1
        else:
            if predict_labels[i] == 'politics':
                FP += 1
            else:
                FN += 1
                
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    F1 = (2 * precision * recall) / (precision + recall)
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    
    print('Performance measure for ' + prediction_file + ':-')
    print('Precision: ' + str(precision))
    print('Recall: ' + str(recall))
    print('F1 Score: ' + str(F1))
    print('Accuracy: ' + str(accuracy))
    
for i in range(len(predictions)):
    calculate_performance(predictions[i], labels[i])
