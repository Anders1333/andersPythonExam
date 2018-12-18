import os, os.path
from flask import Flask, render_template, request
from lib.imagescrape import image_search, testdata_params as tp


def numoffiles(DIR):
    count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    return count

num_of_testdata_files = {
    'fibrin': numoffiles("testdata/fibrin"),
    'necrosis': numoffiles("testdata/fibrin"),
    'superficial': numoffiles("testdata/fibrin")
    }

app = Flask(__name__, template_folder='../templates', static_folder='../testdata')

# Root dir - static page for manually selecting Scrape or Evaluate
@app.route("/")
def idx():
    return render_template('idx.html')


@app.route("/scrape", methods=['GET', 'POST'])

def scrape():
    scrapecomplete = False
    if request.method == "POST":
        wtype = request.form.getlist('type')[0]
        termtp = request.form.getlist('termtype')[0]
        custom = request.form.getlist('custom')[0]
        amount = int(request.form.getlist('amount')[0])

        if termtp == "custom":
            scrapecomplete = image_search(custom, tp[wtype][1], amount)
        else:
            scrapecomplete = image_search(tp[wtype][0], tp[wtype][1], amount)

    return render_template('scrape.html', scrapecomplete=scrapecomplete)



@app.route("/evaluate")

def eval():
    TYPE = request.args.get('type')
    return render_template('eval.html', type=TYPE)



@app.route("/del", methods=['GET', 'POST'])

def delete():
    if request.method == "POST":
        accepted = request.form.getlist('accepted')[0]
        imgnum = request.form.getlist('num')[0]
        TYPE = request.form.getlist('type')[0]

        if accepted == "yes":
            fr = 'unconfirmeddata/' + TYPE + '/' + imgnum + '.jpg'
            to = 'testdata/' + TYPE + '/' + str(num_of_testdata_files[TYPE]) + '.jpg'

            os.rename(fr, to)

        return "OK"

    else:
        return "Error"
