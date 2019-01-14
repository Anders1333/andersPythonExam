# Wound Recognition (Python 3.7.x)
Talented Direction - Anders (cph-ac172) Jonas (cph-ja213) Rune (cph-rm129)


We will make a program to identify wound types based on images, using a machine learning approach.

Users will be able to upload an image, which will then be processed and one of the following wound features wille be identified: 

- Necrosis
- Fibrin
- Superficial(e.g bruises or low-depth wounds)

# Dependencies
This program depends on the folowing modules:

- os, urllib, flask, selenium, numpy, theano, opencv, 
- keras, json, time, urllib, pickle, random

#Installation
`git clone https://github.com/jonasa64/pythonExamProject.git`
or download directly from GitHub

Install dependencies 

# Execution 

Go to the cloned or downloaded directory from a Shell/Terminal commandline
Execute "main.py" with your prefered Python CLI using valid arguments. E.g:

`python main.py webgui` (WebBrowser-based GUI to download and evaluate images for test data markup   
`python main.py get_images` Download images from Google, using default search terms, and a default amount of 100 images per category.
`python main.py training` train and save a model based on the positively evaluated images

`python main.py serve` Serve a WebServer on which to upload and get images assessed. 

`python main.py cleanup` Cleans up image folders to reset - mainly for dev puposes 

