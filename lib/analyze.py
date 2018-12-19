import os, threading
from threading import Thread

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
    print("Removing", imagepath, "...")
    results[imagepath] = ["Picture is good", False]
    os.remove(imagepath)
    print(imagepath, "removed ...")