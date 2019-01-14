import os; os.environ['KERAS_BACKEND'] = 'theano'

import threading, keras, tensorflow, pickle
import numpy as np
from threading import Thread
from keras_preprocessing import image

results = {}  # dictionary to contain results of analyzed images, indexed by session ID

labeling = ['fibrin', 'necrosis', 'superficial']
model = keras.models.load_model("model.kerassave")  # load the Keras model


def analyze(imagepath):
    global results
    threads = [t.getName() for t in threading.enumerate()]  # create a list of currently running threads
    if imagepath in results:  # if image path of session has been added to the results dict, pass result to httprequest
        if results[imagepath][1]:
            if os.path.exists(imagepath):
                print("Removing", imagepath, "...")
                os.remove(imagepath)
                print(imagepath, "removed ...")

            res = results[imagepath][0]
            results.pop(imagepath)  

            return res

        else:
            results[imagepath][1] = True
            return "Done:" + results[imagepath][0]

    elif imagepath in threads:
        return "Analyzing ..."

    else:
        t1 = Thread(name=imagepath, target=analyze_img(imagepath))
        t1.start()
        t1.join()

    return "Analyzing ..."

def load_image(img_path):

    img = image.load_img(img_path, target_size=(100, 100))
    img_theano = image.img_to_array(img)                    # (height, width, channels)
    img_theano = np.expand_dims(img_theano, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_theano /= 255.                                      # imshow expects values in the range [0, 1]

    return img_theano

def max_index(my_list):
    i = 0
    idx = 0
    highest = 0

    for elm in my_list:
        if elm > highest:
            idx = i
            highest = elm

        i += 1

    return idx

def analyze_img(imagepath):
    global results, model, labels, sess

    img = load_image(imagepath)

    predict = model.predict(img)
    predict = [p for p in predict[0]]
    print("Prediction:", predict)
    predict = max_index(predict)
    print("Index:", predict)
    prediction = "Image indicates a " + labeling[predict] + " wound."

    results[imagepath] = [prediction, False]


'''
    img = tensorflow.read_file(imagepath)
    img = tensorflow.image.decode_jpeg(img, channels=3)
    img.set_shape([None, None, 3])
    img = tensorflow.image.resize_images(img, (100, 100))

    print(sess)

    img = img.eval(session=sess)  # convert to numpy array
    img = np.expand_dims(img, 0)  # make 'batch' of 1
'''