import concurrent.futures
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def fetch_horoscope(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    return soup.find('div', class_='article-details').text

def get_horoscope_data(znak, urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_horoscope, urls))

    dnevni, nedeljni, mesecni, godisnji = results

    return render_template('horoskop-detaljno.html', znak=znak, dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)


@app.route('/ovan')
def ovan():
    znak = 'Ovan'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/ovan/',
        'http://www.horoskopius.com/nedeljni-horoskop/ovan/',
        'http://www.horoskopius.com/mesecni-horoskop/ovan/',
        'http://www.horoskopius.com/godisnji-horoskop/ovan/'
    ]
    return get_horoscope_data(znak, urls)


@app.route('/bik')
def bik():
    znak = 'Bik'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/bik/',
        'http://www.horoskopius.com/nedeljni-horoskop/bik/',
        'http://www.horoskopius.com/mesecni-horoskop/bik/',
        'http://www.horoskopius.com/godisnji-horoskop/bik/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/blizanci')
def blizanci():
    znak = 'Blizanci'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/blizanci/',
        'http://www.horoskopius.com/nedeljni-horoskop/blizanci/',
        'http://www.horoskopius.com/mesecni-horoskop/blizanci/',
        'http://www.horoskopius.com/godisnji-horoskop/blizanci/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/rak')
def rak():
    znak = 'Rak'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/rak/',
        'http://www.horoskopius.com/nedeljni-horoskop/rak/',
        'http://www.horoskopius.com/mesecni-horoskop/rak/',
        'http://www.horoskopius.com/godisnji-horoskop/rak/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/lav')
def lav():
    znak = 'Lav'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/lav/',
        'http://www.horoskopius.com/nedeljni-horoskop/lav/',
        'http://www.horoskopius.com/mesecni-horoskop/lav/',
        'http://www.horoskopius.com/godisnji-horoskop/lav/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/devica')
def devica():
    znak = 'Devica'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/devica/',
        'http://www.horoskopius.com/nedeljni-horoskop/devica/',
        'http://www.horoskopius.com/mesecni-horoskop/devica/',
        'http://www.horoskopius.com/godisnji-horoskop/devica/'
    ]
    return get_horoscope_data(znak, urls)




@app.route('/vaga')
def vaga():
    znak = 'Vaga'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/vaga/',
        'http://www.horoskopius.com/nedeljni-horoskop/vaga/',
        'http://www.horoskopius.com/mesecni-horoskop/vaga/',
        'http://www.horoskopius.com/godisnji-horoskop/vaga/'
    ]
    return get_horoscope_data(znak, urls)




@app.route('/skorpija')
def skorpija():
    znak = 'Skorpija'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/skorpija/',
        'http://www.horoskopius.com/nedeljni-horoskop/skorpija/',
        'http://www.horoskopius.com/mesecni-horoskop/skorpija/',
        'http://www.horoskopius.com/godisnji-horoskop/skorpija/'
    ]
    return get_horoscope_data(znak, urls)


@app.route('/strelac')
def strelac():
    znak = 'Strelac'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/strelac/',
        'http://www.horoskopius.com/nedeljni-horoskop/strelac/',
        'http://www.horoskopius.com/mesecni-horoskop/strelac/',
        'http://www.horoskopius.com/godisnji-horoskop/strelac/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/jarac')
def jarac():
    znak = 'Jarac'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/jarac/',
        'http://www.horoskopius.com/nedeljni-horoskop/jarac/',
        'http://www.horoskopius.com/mesecni-horoskop/jarac/',
        'http://www.horoskopius.com/godisnji-horoskop/jarac/'
    ]
    return get_horoscope_data(znak, urls)


@app.route('/vodolija')
def vodolija():
    znak = 'Vodolija'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/vodolija/',
        'http://www.horoskopius.com/nedeljni-horoskop/vodolija/',
        'http://www.horoskopius.com/mesecni-horoskop/vodolija/',
        'http://www.horoskopius.com/godisnji-horoskop/vodolija/'
    ]
    return get_horoscope_data(znak, urls)


@app.route('/ribe')
def ribe():
    znak = 'Ribe'
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/ribe/',
        'http://www.horoskopius.com/nedeljni-horoskop/ribe/',
        'http://www.horoskopius.com/mesecni-horoskop/ribe/',
        'http://www.horoskopius.com/godisnji-horoskop/ribe/'
    ]
    return get_horoscope_data(znak, urls)



if __name__ == '__main__':
    app.run(debug=True)










# import concurrent.futures
# from flask import Flask, render_template
# from bs4 import BeautifulSoup
# import requests
#
# app = Flask(__name__)
#
# def fetch_horoscope(url):
#     source = requests.get(url).text
#     soup = BeautifulSoup(source, 'lxml')
#     return soup.find('div', class_='article-details').text
#
# def get_horoscope_data(znak, urls):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         results = executor.map(fetch_horoscope, urls)
#
#     dnevni, nedeljni, mesecni, godisnji = results
#
#     return render_template('horoskop-detaljno.html', znak=znak, dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)
#
# @app.route('/blizanci')
# def blizanci():
#     znak = 'Blizanci'
#     urls = [
#         'http://www.horoskopius.com/dnevni-horoskop/blizanci/',
#         'http://www.horoskopius.com/nedeljni-horoskop/blizanci/',
#         'http://www.horoskopius.com/mesecni-horoskop/blizanci/',
#         'http://www.horoskopius.com/godisnji-horoskop/blizanci/'
#     ]
#     return get_horoscope_data(znak, urls)
#
# @app.route('/vodolija')
# def vodolija():
#     znak = 'Vodolija'
#     urls = [
#         'http://www.horoskopius.com/dnevni-horoskop/vodolija/',
#         'http://www.horoskopius.com/nedeljni-horoskop/vodolija/',
#         'http://www.horoskopius.com/mesecni-horoskop/vodolija/',
#         'http://www.horoskopius.com/godisnji-horoskop/vodolija/'
#     ]
#     return get_horoscope_data(znak, urls)
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
