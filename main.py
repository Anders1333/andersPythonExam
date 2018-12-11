import sys
from lib import cleanup
from lib.imagescrape import image_search

# Search parameters & testdata folders

necrotic = ['necrotic wound human skin', "testdata/necrosis/"]
fibrin = ['sår med fibrin', "testdata/fibrin/"]
superficial = ['overfladiske sår hud', "testdata/superficial/"]

if __name__ == '__main__':

    if sys.argv[1] == "cleanup":
        cleanup.do(necrotic[1])
        cleanup.do(fibrin[1])
        cleanup.do(superficial[1])

    if sys.argv[1] == "get_images":
        image_search(necrotic[0], 200, necrotic[1])
        image_search(fibrin[0], 200, fibrin[1])
        image_search(superficial[0], 200, superficial[1])
