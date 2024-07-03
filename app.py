from flask import Flask, render_template, jsonify
import json
from datetime import datetime
from horoskop import ovan, bik, blizanci, rak, lav, devica, vaga, skorpija, strelac, jarac, vodolija, ribe


app = Flask(__name__)


@app.context_processor
def inject_now():
    return {'now': datetime.now()}


@app.route('/znak/<znak>')
def prikazi_znak(znak):
    with open('data/horoskop.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    if znak in data:
        return render_template('znak.html', znak=data[znak])
    else:
        return "Znak nije pronađen."


@app.route('/')

def index():
    return render_template('index.html')




@app.route('/ovan')
def ov():
    return ovan()


@app.route('/bik')
def bi():
    return bik()


@app.route('/blizanci')
def bliz():
    return blizanci()


@app.route('/rak')
def ra():
    return rak()


@app.route('/lav')
def la():
    return lav()


@app.route('/devica')
def dev():
    return devica()


@app.route('/vaga')
def va():
    return vaga()


@app.route('/skorpija')
def sko():
    return skorpija()


@app.route('/strelac')
def str():
    return strelac()


@app.route('/jarac')
def jar():
    return jarac()

@app.route('/vodolija')
def vodo():
    return vodolija()

@app.route('/ribe')
def ri():
    return ribe()


if __name__ == '__main__':
    app.run()
