'''
Fast deletion of images in the testdata folders
Mainly for development purposes (e.g. before git push)
'''

from lib.imagescrape import testdata_params as tp
import os

# tp contains the image paths in which the testdata is stored


def do(folder):
    '''
    Deletes all files of a folder
    :param folder: path to folder to delete files in
    :return: returns True when done
    '''
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.exists(path):
            os.remove(path)

    return True

def all():
    '''
    Deletes all images used for testing and training
    :return: returns True when done
    '''
    do('static/testdata/' + tp['necrotic'][1])
    do('static/testdata/' + tp['fibrin'][1])
    do('static/testdata/' + tp['superficial'][1])
    do('static/unconfirmeddata/' + tp['necrotic'][1])
    do('static/unconfirmeddata/' + tp['fibrin'][1])
    do('static/unconfirmeddata/' + tp['superficial'][1])

    return True