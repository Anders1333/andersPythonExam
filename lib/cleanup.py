'''
Fast deletion of images in the testdata folders
Mainly for development purposes (e.g. before git push)
'''

from lib.imagescrape import testdata_params as tp
import os

def do(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.exists(path):
            os.remove(path)

    return True

def all():
    do('static/testdata/' + tp['necrotic'][1])
    do('static/testdata/' + tp['fibrin'][1])
    do('static/testdata/' + tp['superficial'][1])
    do('static/unconfirmeddata/' + tp['necrotic'][1])
    do('static/unconfirmeddata/' + tp['fibrin'][1])
    do('static/unconfirmeddata/' + tp['superficial'][1])

    return True