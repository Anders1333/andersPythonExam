import os, threading, keras, tensorflow, pickle
import numpy as np
from threading import Thread
# from lib.keros_implementation import setup_load_cifa
results = {}

def analyze(imagepath):
    global results
    threads = [t.getName() for t in threading.enumerate()]
    if imagepath in results:
        if results[imagepath][1]:
            return results[imagepath][0]
        else:
            results[imagepath][1] = True
            return "Done:" + results[imagepath][0]

    elif imagepath in threads:
        "Analyzing ..."

    else:
        t1 = Thread(name=imagepath, target=analyze_img(imagepath))
        t1.start()
        t1.join()

    return "Analyzing ..."

def analyze_img(imagepath):
    global results

    sess = keras.backend.get_session()

    model = keras.models.load_model()
    with open("y.pickle", mode="rb") as f:
        labels = pickle.load(f)

    img = tensorflow.read_file(imagepath)
    img = tensorflow.image.decode_jpeg(img, channels=3)
    img.set_shape([None, None, 3])
    img = tensorflow.image.resize_images(img, (32, 32))
    img = img.eval(session=sess)  # convert to numpy array
    img = np.expand_dims(img, 0)  # make 'batch' of 1

    pred = model.predict(img)
    pred = labels["label_names"][np.argmax(pred)]
    prediction = "Image indicates a " + pred + " wound."

    print("Removing", imagepath, "...")
    results[imagepath] = [prediction, False]
    os.remove(imagepath)
    print(imagepath, "removed ...")

    return True