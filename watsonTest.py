from watson_developer_cloud import VisualRecognitionV3 as vr
import json
instance = vr(iam_apikey='yBWlRyLU6O-LsI75eUhcWRr8K-pGwOFrv9Fb_7M8aigD', version='2016-05-20')


def watson():
    with open('/testdata/beagle.zip', 'rb') as beagle, open(
            '/testdata/goldenretriever.zip', 'rb') as goldenretriever, open(
                '/testdata/husky.zip', 'rb') as husky, open(
                    '/testdata/cats.zip', 'rb') as cats:
        model = instance.create_classifier(
            'dogs',
            beagle_positive_examples=beagle,
            goldenretriever_positive_examples=goldenretriever,
          husky_positive_examples=husky,
            negative_examples=cats
            ).get_result()
    print(json.dumps(model, indent=2))
