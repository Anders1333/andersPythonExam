import sys, webbrowser
from lib import cleanup, evaluate
from lib.imagescrape import image_search, testdata_params as tp


if __name__ == '__main__':
    if sys.argv[1] == "image_gui":
        webbrowser.open('http://127.0.0.1:5000/')
        evaluate.app.run()

    if sys.argv[1] == "cleanup":
        cleanup.do(tp['necrotic'][1])
        cleanup.do(tp['fibrin'][1])
        cleanup.do(tp['superficial'][1])

    if sys.argv[1] == "get_images":
        image_search(tp['necrotic'][0], tp['necrotic'][1])
        image_search(tp['fibrin'][0], tp['fibrin'][1])
        image_search(tp['superficial'][0], tp['superficial'][1])