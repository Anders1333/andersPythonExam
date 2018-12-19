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



#NAME = "fibrin-vs-necrosis-vs-superficial-3x64Conv2D{}".format(int( time.time()))
#tensorBord = TensorBoard(log_dir="logs/{}".format(NAME))

DATA_DIR = 'static/testdata'
CATEGORIES = ['fibrin', 'necrosis','superficial']




IMG_SIZE = 100



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

#print(len(training_data))
 
random.shuffle(training_data)

for sample in training_data:
    print(sample[1])
    
    
x = []
y = []

def resize(x,y):
    for features, label in training_data:
        x.append(features)
        y.append(label)
    
resize(x,y)    
x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE,1)
def pickle_file(x , y):
    pickle_out = open("X.pickle","wb")
    pickle.dump(x, pickle_out)
    pickle_out.close()
    
    pickle_out = open("y.pickle","wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()


    pickle_in = open("X.pickle","rb")
    x = pickle.load(pickle_in)
    
    pickle_in = open("y.pickle","rb")
    y = pickle.load(pickle_in)


pickle_file(x,y)

x = x /255.0
def trainig_the_model():
    model = Sequential()
    model.add(Conv2D(64, (3,3), input_shape=x.shape[1:]))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(64, (3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(64, (3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    model.fit(x,y, batch_size=32, epochs=7, validation_split=0.1)

    

