import sys
from lib import cleanup
from lib.imagescrape import image_search
import training_images as ti
# Search parameters & testdata folders

necrotic = ['necrotic wound human skin', "testdata/necrosis/"]
fibrin = ['sår med fibrin', "testdata/fibrin/"]
superficial = ['overfladiske sår hud', "testdata/superficial/"]


DATA_DIR = 'C:/Users/hp/Pictures/testdata'
CATEGORIES = ['fibrin', 'necrosis','superficial']

x = []
y = []

if __name__ == '__main__':

    if sys.argv[1] == "cleanup":
        cleanup.do(necrotic[1])
        cleanup.do(fibrin[1])
        cleanup.do(superficial[1])

    if sys.argv[1] == "get_images":
        image_search(necrotic[0], 200, necrotic[1])
        image_search(fibrin[0], 200, fibrin[1])
        image_search(superficial[0], 200, superficial[1])
    if sys.argv[1] == "training":
        ti.create_training_data(DATA_DIR, CATEGORIES)
        ti.resize(x,y)
        ti.pickle_file(x,y)
        ti.trainig_the_model()