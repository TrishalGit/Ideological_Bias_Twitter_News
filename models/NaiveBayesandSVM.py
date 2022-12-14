import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import os

directory = os.getcwd()

"""## Train Left"""

#df_left_train = pd.read_csv(directory + '/../data/train_test_split/Left_Train.csv',header=None)
df_left_train = pd.read_csv(directory + '/../data/train_test_split/Left_Harvard_Train.csv',header=None)

df_left_train

tweets_ltrain = []
topics_ltrain = []
for index, row in df_left_train.iterrows():
    tweets_ltrain.append(row[0])
    topics_ltrain.append(row[1])

#df_left_test = pd.read_csv(directory + '/../data/train_test_split/Left_Test.csv',header=None)
df_left_test = pd.read_csv(directory + '/../data/train_test_split/Left_Harvard_Test.csv',header=None)

df_left_test

tweets_ltest = []
topics_ltest = []
for index, row in df_left_test.iterrows():
    tweets_ltest.append(row[0])
    topics_ltest.append(row[1])

#df_right_test = pd.read_csv(directory + '/../data/train_test_split/Right_Test.csv',header=None)
#df_neutral_test = pd.read_csv(directory + '/../data/train_test_split/Neutral_Test.csv',header=None)
df_right_test = pd.read_csv(directory + '/../data/train_test_split/Right_Harvard_Test.csv',header=None)
df_neutral_test = pd.read_csv(directory + '/../data/train_test_split/Neutral_Harvard_Test.csv',header=None)

tweets_rtest = []
topics_rtest = []
for index, row in df_right_test.iterrows():
    tweets_rtest.append(row[0])
    topics_rtest.append(row[1])

tweets_ntest = []
topics_ntest = []
for index, row in df_neutral_test.iterrows():
    tweets_ntest.append(row[0])
    topics_ntest.append(row[1])

Train_X, Train_Y = tweets_ltrain, topics_ltrain
L_Test_X, L_Test_Y = tweets_ltest, topics_ltest
R_Test_X, R_Test_Y = tweets_rtest, topics_rtest
N_Test_X, N_Test_Y = tweets_ntest, topics_ntest

from sklearn.preprocessing import LabelEncoder
Encoder = LabelEncoder()
Train_Y = Encoder.fit_transform(Train_Y)
L_Test_Y = Encoder.fit_transform(L_Test_Y)
R_Test_Y = Encoder.fit_transform(R_Test_Y)
N_Test_Y = Encoder.fit_transform(N_Test_Y)
# world : 1 politics: 0

Tfidf_vect = TfidfVectorizer()
Tfidf_vect.fit(tweets_ltrain)
Train_X_Tfidf = Tfidf_vect.transform(Train_X)
L_Test_X_Tfidf = Tfidf_vect.transform(L_Test_X)
R_Test_X_Tfidf = Tfidf_vect.transform(R_Test_X)
N_Test_X_Tfidf = Tfidf_vect.transform(N_Test_X)

Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Tfidf,Train_Y)

SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Tfidf,Train_Y)

"""Test on left"""

predictions_NB = Naive.predict(L_Test_X_Tfidf)
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, L_Test_Y)*100)
print("Naive Bayes F1 Score -> ",f1_score(predictions_NB, L_Test_Y))

predictions_SVM = SVM.predict(L_Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, L_Test_Y)*100)
print("SVM F1 Score -> ",f1_score(predictions_SVM, L_Test_Y))

"""Test on right"""

predictions_NB = Naive.predict(R_Test_X_Tfidf)
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, R_Test_Y)*100)
print("Naive Bayes F1 Score -> ",f1_score(predictions_NB, R_Test_Y))

predictions_SVM = SVM.predict(R_Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, R_Test_Y)*100)
print("SVM F1 Score -> ",f1_score(predictions_SVM, R_Test_Y))

"""Test on Neutral"""

predictions_NB = Naive.predict(N_Test_X_Tfidf)
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, N_Test_Y)*100)
print("Naive Bayes F1 Score -> ",f1_score(predictions_NB, N_Test_Y))

predictions_SVM = SVM.predict(N_Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, N_Test_Y)*100)
print("SVM F1 Score -> ",f1_score(predictions_SVM, N_Test_Y))

"""## Train right"""

#df_right_train = pd.read_csv(directory + '/../data/train_test_split/Right_Train.csv',header=None)
df_right_train = pd.read_csv(directory + '/../data/train_test_split/Right_Harvard_Train.csv',header=None)

tweets_rtrain = []
topics_rtrain = []
for index, row in df_right_train.iterrows():
    tweets_rtrain.append(row[0])
    topics_rtrain.append(row[1])

R_Train_X, R_Train_Y = tweets_rtrain, topics_rtrain
R_Train_Y = Encoder.fit_transform(R_Train_Y)
Tfidf_vect_R = TfidfVectorizer()
Tfidf_vect_R.fit(tweets_rtrain)
R_Train_X_Tfidf = Tfidf_vect_R.transform(R_Train_X)
L_Test_X_Tfidf = Tfidf_vect_R.transform(L_Test_X)
R_Test_X_Tfidf = Tfidf_vect_R.transform(R_Test_X)
N_Test_X_Tfidf = Tfidf_vect_R.transform(N_Test_X)

Naive.fit(R_Train_X_Tfidf,R_Train_Y)

SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(R_Train_X_Tfidf,R_Train_Y)

"""Test on right"""

predictions_NB = Naive.predict(R_Test_X_Tfidf)
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, R_Test_Y)*100)
print("Naive Bayes F1 Score -> ",f1_score(predictions_NB, R_Test_Y))

predictions_SVM = SVM.predict(R_Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, R_Test_Y)*100)
print("SVM F1 Score -> ",f1_score(predictions_SVM, R_Test_Y))

"""Test on left"""

predictions_NB = Naive.predict(L_Test_X_Tfidf)
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, L_Test_Y)*100)
print("Naive Bayes F1 Score -> ",f1_score(predictions_NB, L_Test_Y))

predictions_SVM = SVM.predict(L_Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, L_Test_Y)*100)
print("SVM F1 Score -> ",f1_score(predictions_SVM, L_Test_Y))

"""Test on Neutral"""

predictions_NB = Naive.predict(N_Test_X_Tfidf)
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, N_Test_Y)*100)
print("Naive Bayes F1 Score -> ",f1_score(predictions_NB, N_Test_Y))

predictions_SVM = SVM.predict(N_Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, N_Test_Y)*100)
print("SVM F1 Score -> ",f1_score(predictions_SVM, N_Test_Y))

"""## Train on Neutral"""

#df_neutral_train = pd.read_csv(directory + '/../data/train_test_split/Neutral_Train.csv',header=None)
df_neutral_train = pd.read_csv(directory + '/../data/train_test_split/Neutral_Harvard_Train.csv',header=None)

tweets_ntrain = []
topics_ntrain = []
for index, row in df_neutral_train.iterrows():
    tweets_ntrain.append(row[0])
    topics_ntrain.append(row[1])

N_Train_X, N_Train_Y = tweets_ntrain, topics_ntrain
N_Train_Y = Encoder.fit_transform(N_Train_Y)
Tfidf_vect_N = TfidfVectorizer()
Tfidf_vect_N.fit(tweets_ntrain)
N_Train_X_Tfidf = Tfidf_vect_N.transform(N_Train_X)
L_Test_X_Tfidf = Tfidf_vect_N.transform(L_Test_X)
R_Test_X_Tfidf = Tfidf_vect_N.transform(R_Test_X)
N_Test_X_Tfidf = Tfidf_vect_N.transform(N_Test_X)

Naive.fit(N_Train_X_Tfidf,N_Train_Y)

SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(N_Train_X_Tfidf,N_Train_Y)

"""Test on right"""

predictions_NB = Naive.predict(R_Test_X_Tfidf)
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, R_Test_Y)*100)
print("Naive Bayes F1 Score -> ",f1_score(predictions_NB, R_Test_Y))

predictions_SVM = SVM.predict(R_Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, R_Test_Y)*100)
print("SVM F1 Score -> ",f1_score(predictions_SVM, R_Test_Y))

"""Test on left"""

predictions_NB = Naive.predict(L_Test_X_Tfidf)
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, L_Test_Y)*100)
print("Naive Bayes F1 Score -> ",f1_score(predictions_NB, L_Test_Y))

predictions_SVM = SVM.predict(L_Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, L_Test_Y)*100)
print("SVM F1 Score -> ",f1_score(predictions_SVM, L_Test_Y))

"""Test on neutral"""

predictions_NB = Naive.predict(N_Test_X_Tfidf)
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, N_Test_Y)*100)
print("Naive Bayes F1 Score -> ",f1_score(predictions_NB, N_Test_Y))

predictions_SVM = SVM.predict(N_Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, N_Test_Y)*100)
print("SVM F1 Score -> ",f1_score(predictions_SVM, N_Test_Y))
