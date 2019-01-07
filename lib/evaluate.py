import os, os.path
from flask import Flask, render_template, request
from lib.imagescrape import image_search, testdata_params as tp


def numoffiles(DIR):
    count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    return count

num_of_testdata_files = {
    'fibrin': numoffiles("static/testdata/fibrin"),
    'necrosis': numoffiles("static/testdata/necrosis"),
    'superficial': numoffiles("static/testdata/superficial")
    }

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Root dir - static page for manually selecting Scrape or Evaluate
@app.route("/")
def idx():
    return render_template('idx.html')


@app.route("/scrape", methods=['GET', 'POST'])

def scrape():
    scrapecomplete = 'False'
    if request.method == "POST":
        wtype = request.form.getlist('type')[0]
        termtp = request.form.getlist('termtype')[0]
        custom = request.form.getlist('custom')[0]
        amount = int(request.form.getlist('amount')[0])

        if termtp == "custom":
            scrapecomplete = image_search(custom, tp[wtype][1], amount)
        else:
            scrapecomplete = image_search(tp[wtype][0], tp[wtype][1], amount)

        if scrapecomplete == 'False':
            scrapecomplete = "Error"

    return render_template('scrape.html', scrapecomplete=scrapecomplete)



@app.route("/evaluate")

def eval():
    TYPE = request.args.get('type')
    try:
        typeimages = os.listdir("static/unconfirmeddata/" + TYPE)
    except:
        typeimages = 0

    return render_template('eval.html', type=TYPE, typeimages=typeimages)



@app.route("/del", methods=['GET', 'POST'])

def delete():
    if request.method == "POST":
        accepted = request.form.getlist('accepted')[0]
        img = request.form.getlist('img')[0]
        TYPE = request.form.getlist('type')[0]
        fr = 'static/unconfirmeddata/' + TYPE + '/' + img

        if accepted == "yes":
            to = 'static/testdata/' + TYPE + '/' + str(num_of_testdata_files[TYPE] + 1) + '.jpg'
            num_of_testdata_files[TYPE] += 1
            os.rename(fr, to)
        else:
            os.remove(fr)

        return "OK"

    else:
        return "Error"
