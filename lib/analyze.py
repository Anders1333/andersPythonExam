import os, threading
from threading import Thread

results = {}

def analyze(imagepath):
    global results
    threads = [t.getName() for t in threading.enumerate()]
    if imagepath in results:
        return results[imagepath]

    elif imagepath in threads:
        "Analyzing ..."

    else:
        t1 = Thread(name=imagepath, target=analyze_img(imagepath))
        t1.start()
        t1.join()

    return "Analyzing ..."

def analyze_img(imagepath):
    global results
    results[imagepath] = "Done: Picture is good"
    os.remove(imagepath)