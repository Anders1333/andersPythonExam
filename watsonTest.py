from watson_developer_cloud import VisualRecognitionV3 as vr
import json
instance = vr(iam_apikey='yBWlRyLU6O-LsI75eUhcWRr8K-pGwOFrv9Fb_7M8aigD', version='2016-05-20')

#img = instance.classify(url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/40524640/1/?bust=1514432903')
#
#
#print(img)




    
with open('C:/Users/hp/Pictures/testdata/beagle.zip', 'rb') as beagle, open(
        'C:/Users/hp/Pictures/testdata/goldenretriever.zip', 'rb') as goldenretriever, open(
            'C:/Users/hp/Pictures/testdata/husky.zip', 'rb') as husky, open(
                'C:/Users/hp/Pictures/testdata/cats.zip', 'rb') as cats:
    model = instance.create_classifier(
        'dogs',
        beagle_positive_examples=beagle,
        goldenretriever_positive_examples=goldenretriever,
      husky_positive_examples=husky,
        negative_examples=cats
        ).get_result()
print(json.dumps(model, indent=2))
