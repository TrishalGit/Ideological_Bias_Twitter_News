from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
# df = pd.read_csv('/content/drive/MyDrive/train_test_split/Left_Train.csv',header=None)
df = pd.read_csv('/content/drive/MyDrive/train_test_split/Left_Harvard_Train.csv',header=None)

df

df[2]=df[1].apply(lambda x: 1 if x=='world' else 0)
df.head()

# df_test = pd.read_csv('/content/drive/MyDrive/train_test_split/Left_Test.csv',header=None)
df_test = pd.read_csv('/content/drive/MyDrive/train_test_split/Left_Harvard_Test.csv',header=None)

df_test[2]=df_test[1].apply(lambda x: 1 if x=='world' else 0)
df_test

from sklearn.model_selection import train_test_split
X_train, y_train = df[0], df[2]
X_test, y_test = df_test[0], df_test[2]
X_train.head(4)

!pip install -U tensorflow
!pip install -U tensorflow-text
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text

bert_preprocess = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
bert_encoder = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4")

# Bert layers
text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
preprocessed_text = bert_preprocess(text_input)
outputs = bert_encoder(preprocessed_text)
# Neural network layers
l = tf.keras.layers.Dropout(0.1, name="dropout")(outputs['pooled_output'])
l = tf.keras.layers.Dense(1, activation='sigmoid', name="output")(l)
# inputs and outputs to construct a final model
model = tf.keras.Model(inputs=[text_input], outputs = [l])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size = 32)

y_predicted = model.predict(X_test)
y_predicted = y_predicted.flatten()
print(y_predicted)

BERT_pred = []
for i in y_predicted:
  if i>0.5:
    BERT_pred.append(1)
  else:
    BERT_pred.append(0)

"""Test on left"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
print("Bert Accuracy Score -> ",accuracy_score(BERT_pred, y_test)*100)
print("F1 Score -> ",f1_score(BERT_pred, y_test))

"""Test on Neutral"""

# df_test_N = pd.read_csv('/content/drive/MyDrive/train_test_split/Neutral_Test.csv',header=None)
df_test_N = pd.read_csv('/content/drive/MyDrive/train_test_split/Neutral_Harvard_Test.csv',header=None)
df_test_N

df_test_N[2]=df_test_N[1].apply(lambda x: 1 if x=='world' else 0)
df_test_N

X_test_N, y_test_N = df_test_N[0], df_test_N[2]

y_predicted_N = model.predict(X_test_N)
y_predicted_N = y_predicted_N.flatten()
print(y_predicted_N)

BERT_pred_N = []
for i in y_predicted_N:
  if i>0.5:
    BERT_pred_N.append(1)
  else:
    BERT_pred_N.append(0)

print("Bert Accuracy Score -> ",accuracy_score(BERT_pred_N, y_test_N)*100)
print("F1 Score -> ",f1_score(BERT_pred_N, y_test_N))

"""Test on right"""

# df_test_R = pd.read_csv('/content/drive/MyDrive/train_test_split/Right_Test.csv',header=None)
df_test_R = pd.read_csv('/content/drive/MyDrive/train_test_split/Right_Harvard_Test.csv',header=None)
df_test_R

df_test_R[2]=df_test_R[1].apply(lambda x: 1 if x=='world' else 0)
df_test_R

X_test_R, y_test_R = df_test_R[0], df_test_R[2]

y_predicted_R = model.predict(X_test_R)
y_predicted_R = y_predicted_R.flatten()
# print(y_predicted_R)

BERT_pred_R = []
for i in y_predicted_R:
  if i>0.5:
    BERT_pred_R.append(1)
  else:
    BERT_pred_R.append(0)

print("Bert Accuracy Score -> ",accuracy_score(BERT_pred_R, y_test_R)*100)
print("F1 Score -> ",f1_score(BERT_pred_R, y_test_R))
