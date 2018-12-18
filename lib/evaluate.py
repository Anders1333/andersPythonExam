from flask import Flask, render_template, request
from lib.imagescrape import image_search, testdata_params as tp

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

        print(wtype, termtp, custom, amount)

        if termtp == "custom":
            scrapecomplete = image_search(custom, tp[wtype][1], amount)
        else:
            scrapecomplete = image_search(tp[wtype][0], tp[wtype][1], amount)

    return render_template('scrape.html', scrapecomplete=scrapecomplete)



@app.route("/evaluate")

def eval():
    tp = request.args.get('type')
    return render_template('eval.html', type=tp)
