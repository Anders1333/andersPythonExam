
import json
import time
from watson_developer_cloud import VisualRecognitionV3,WatsonApiException


def askTheDoctor(path):
 visual_recognition = VisualRecognitionV3('2016-05-20', iam_apikey='77X3i6DnYWZa0LIHPEnoCbXRqMk_CvVuovLxpH5tOT6K')
 with open(path, 'rb') as image:
    try:
        response = visual_recognition.classify(image, threshold=0.0) # could also be url
        
        if path[-3:] == 'zip':
            doctorTalkMany(response)
        else:  doctorTalkSingle(response)
        
    except WatsonApiException as ex:
        print ("" + ex.code + ex.message + ex.info)

def doctorTalkSingle(response):
   
    name = response.result["images"][0]["classifiers"][0]["classes"][0]["class"]
    score = response.result["images"][0]["classifiers"][0]["classes"][0]["score"]
    name2 = response.result["images"][0]["classifiers"][0]["classes"][1]["class"]
    name3 = response.result["images"][0]["classifiers"][0]["classes"][2]["class"]
    name4 = response.result["images"][0]["classifiers"][0]["classes"][3]["class"]
    name5 = response.result["images"][0]["classifiers"][0]["classes"][4]["class"]
    
    print ("Hmm... Im {}% sure that it is {}.".format(score*100,name))
    time.sleep(3)
    print("Could also just be {}...".format(name2))
    time.sleep(3)
    print("Im certain that it is related to the word: {}".format(name3))
    time.sleep(3)
    print("Im getting a hint of {}... and {}...".format(name4,name5))
    time.sleep(3)

def askTheFaceExpert(path):
 visual_recognition = VisualRecognitionV3('2016-05-20', iam_apikey='77X3i6DnYWZa0LIHPEnoCbXRqMk_CvVuovLxpH5tOT6K')
 with open(path, 'rb') as image:
    try:
        response = visual_recognition.detect_faces(image, threshold=0.0) # could also be url
        doctorTalkFaces(response)
        
        
    except WatsonApiException as ex:
        print ("" + ex.code + ex.message + ex.info)


def doctorTalkMany(response):
    resultDict = response.result["images"]
    for x in resultDict:
        print("\nPicture name: {} ... \nI see {} with {} % certainty".format((x["image"][-11:]), x["classifiers"][0]["classes"][0]["class"], x["classifiers"][0]["classes"][0]["score"]*100))
        time.sleep(2)

def doctorTalkFaces(response):
    resultDict = response.result["images"]
    for x in resultDict:
     print("\nPicture Name: {} ...".format(x["image"][-10:]))
     time.sleep(2)
     print("\nIm {}% sure that it is a {}".format(int(x["faces"][0]["gender"]["score"]*100),x["faces"][0]["gender"]["gender"]))
     time.sleep(2)
     print("\nIm {}% sure this person is between {} and {} years old".format(int(x["faces"][0]["age"]["score"]*100),x["faces"][0]["age"]["min"],x["faces"][0]["age"]["max"]))
     time.sleep(2)

def createClass():
  visual_recognition = VisualRecognitionV3('2016-05-20', iam_apikey='77X3i6DnYWZa0LIHPEnoCbXRqMk_CvVuovLxpH5tOT6K')
    
  try:
        response = visual_recognition.create_classifier(name="detect_skin", 
        necrosis_positive_examples="./images/necrosis.zip",
        fibrin_positive_examples="./images/fibrin.zip",
        superficial_positive_examples="./images/superficial.zip",
        negative_examples_filename="./images/monkeyBunch.zip",
        threshold=0.0) 
        print(response)
        
  except WatsonApiException as ex:
        print ("code: {} message: {} Info: {}".format(ex.code,ex.message,ex.info))
    
  
    

if __name__ == "__main__":
  
   print("We start with a single image:")
   
   askTheDoctor("./images/pug.jpg")  
  
   print("\n--------Now for a zip with many pictures:-------")
  
   askTheDoctor("./images/monkeyBunch.zip")
   
   print("\n----------Now for face recognition:--------")
   
   askTheFaceExpert("./images/faces.zip")
   
   time.sleep(3)
   
   print("---------------Lets train watson!--------------------")
   
   createClass()
    
    
  




            