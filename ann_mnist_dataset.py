# -*- coding: utf-8 -*-
"""ANN-MNIST_Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1axglitEDLay_6I-ngeX4UcqV8ILk682f
"""

import cv2
import keras
import numpy as np
import pandas as pd
from keras.layers import Dense
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

mnist = pd.read_csv('/content/sample_data/mnist_train_small.csv').iloc[:,:].values
mnist

y = mnist[:,0]
x = mnist[:,1:]
y

y_ = to_categorical(y)
print(y_)

y_.shape

temp = x[2]
temp.shape

temp = temp.reshape(28,28)
temp.shape

plt.imshow(temp)

model = Sequential()
model.add(Dense(64, input_dim=784, activation = 'relu'))
model.add(Dense(60, activation = 'relu'))
model.add(Dense(40, activation = 'relu'))
model.add(Dense(20, activation = 'relu'))
model.add(Dense(10,  activation = 'softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

model.summary()

X_train,X_test,y_train,y_test = train_test_split(x,y_,shuffle = True, test_size = 0.1)

history = model.fit(X_train,y_train, validation_data=(X_test,y_test),epochs=30,batch_size =50)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model acc')
plt.ylabel('acc')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

model.save_weights('mnist_1_94.h5')

all_img = []
for i in range(1,10):
  img1 = cv2.imread(str(i)+'.jpg',0)
  (thresh, im_bw) = cv2.threshold(img1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  inv = cv2.bitwise_not(im_bw)
  all_img.append(cv2.resize(inv, (28,28)))

all_img = np.array(all_img)

temp = all_img[0].flatten()
temp = np.reshape(temp,(1,784))
model.predict(temp)

for i in range(1,10):
  plt.subplot(1,10,i)
  plt.imshow(all_img[i-1])
  plt.title(np.argmax(model.predict(np.reshape(all_img[i-1],(1,784)))))