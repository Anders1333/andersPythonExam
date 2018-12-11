# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 01:19:59 2018

@author: hp
"""

import numpy as np
import os
import cv2
import random
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle

DATA_DIR = 'C:/Users/hp/Pictures/testdata'
CATEGORIES = ['fibrin', 'necrosis','superficial']




IMG_SIZE = 70



training_data = []

def create_training_data():
    
    for categorie in CATEGORIES:
        path = os.path.join(DATA_DIR, categorie)
        class_num = CATEGORIES.index(categorie)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
            
create_training_data()

print(len(training_data))
 
random.shuffle(training_data)

for sample in training_data:
    print(sample[1])
    
    
x = []
y = []


for features, label in training_data:
    x.append(features)
    y.append(label)
    
x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE,1)

pickle_out = open("X.pickle","wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()


pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

X = x /255.0

model = Sequential()
model.add(Conv2D(256, (3,3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(256, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X,y, batch_size=32, epochs=5, validation_split=0.1)

