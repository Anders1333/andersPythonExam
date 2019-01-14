import sys, webbrowser
from lib import cleanup, evaluate, serve
from lib.imagescrape import image_search, testdata_params as tp
import training_images as ti


DATA_DIR = 'static/testdata'
CATEGORIES = ['fibrin', 'necrosis', 'superficial']

x = []
y = []

if __name__ == '__main__':
    '''
    Parameters for running the program:
    
    webgui spins up a simple web server and opens it to use as GUI for evaluating and downloading images
    cleanup deletes all images used for testing and training
    get_images runs a pre-defined search and download of images on google, downloading 200 images for each category
    train trains the model, and is to be used when sufficient test data is available
    serve spins up a web server, on which users can upload images and have them evaluated against the trained model
    '''
    if sys.argv[1] == "webgui":
        webbrowser.open('http://127.0.0.1:5000/')
        evaluate.app.run()

    if sys.argv[1] == "cleanup":
        cleanup.all()

    if sys.argv[1] == "get_images":
        image_search(tp['necrotic'][0], tp['necrotic'][1])
        image_search(tp['fibrin'][0], tp['fibrin'][1])
        image_search(tp['superficial'][0], tp['superficial'][1])

    if sys.argv[1] == "train":
        if sys.argv[2].isdigit():
            epochs = int(sys.argv[2])
        else:
            epochs = 10
        ti.train(DATA_DIR, CATEGORIES, epochs)

    if sys.argv[1] == "serve":
        serve.app.run('0.0.0.0')
