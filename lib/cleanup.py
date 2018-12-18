'''
Fast deletion of images in the testdata folders
Mainly for development purposes (e.g. before git push)
'''

import os

def do(folder):
    i = 0
    while True:
        i += 1
        file = folder + "/" + str(i) + ".jpg"
        if os.path.exists(file):
            os.remove(file)
        else:
            break;