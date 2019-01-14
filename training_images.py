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
from keras.utils import to_categorical
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
import pickle

IMG_SIZE = 100


def train(data_dir, categories, epochs):
    training_data = create_training_data(data_dir, categories)
    random.shuffle(training_data)

    x = []
    y = []

    x, y = resize(x, y, training_data)
    x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 3)

    x, y = pickle_file(x, y)
    x = x / 255.0

    training_the_model(x, y, epochs)

    return True


def create_training_data(data_dir, categories):
    training_data = []

    for category in categories:
        path = os.path.join(data_dir, category)  # create path to fibrin', 'necrosis' and 'superficial
        class_num = categories.index(category)

        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_COLOR)  # convert to array
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])  # add this to our training_data
            except:
                pass

    return training_data


def resize(x,y, training_data):
    for features, label in training_data:
        x.append(features)
        y.append(label)

    return x, y


def pickle_file(x, y):
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

    return x, y


def training_the_model(x, y, epochs=10):
    model = Sequential()
    model.add(Conv2D(64, (3, 3), input_shape=x.shape[1:]))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten()) #converts to 1D feature vectors
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(3))
    model.add(Activation('sigmoid'))
    
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    model.fit(x, to_categorical(y), batch_size=32, epochs=epochs, validation_split=0.1)
    model.save("model.kerassave")

    return model

    

