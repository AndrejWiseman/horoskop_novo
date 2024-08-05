import concurrent.futures
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def fetch_horoscope(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    # return soup.find('div', class_='entry-content').text

    entry_content_div = soup.find('div', class_='entry-content')
    paragraphs = entry_content_div.find_all('p', recursive=False)
    # return ' '.join([p.text for p in paragraphs])

    formatted_paragraphs = []
    for p in paragraphs:
        formatted_text = ''
        for content in p.contents:
            if content.name == 'strong':
                formatted_text += f'<strong style="font-weight: bold;">{content.text}</strong><br>'
            else:
                formatted_text += str(content)
        formatted_paragraphs.append(f'<p>{formatted_text}</p>')

    return ' '.join(formatted_paragraphs)



def get_horoscope_data(znak, urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_horoscope, urls))

    dnevni, sutra, nedeljni, mesecni, godisnji = results

    return render_template('horoskop-detaljno.html', znak=znak, dnevni=dnevni, sutra=sutra, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)


@app.route('/ovan')
def ovan():
    znak = 'Ovan'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-ovan/',
        'https://www.astroputnik.com/horoskop-za-sutra-ovan/',
        'https://www.astroputnik.com/nedeljni-horoskop-ovan/',
        'https://www.astroputnik.com/mesecni-horoskop-ovan/',
        'https://www.astroputnik.com/godisnji-horoskop-ovan/'
    ]
    return get_horoscope_data(znak, urls)


@app.route('/bik')
def bik():
    znak = 'Bik'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-bik/',
        'https://www.astroputnik.com/horoskop-za-sutra-bik/',
        'https://www.astroputnik.com/nedeljni-horoskop-bik/',
        'https://www.astroputnik.com/mesecni-horoskop-bik/',
        'https://www.astroputnik.com/godisnji-horoskop-bik/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/blizanci')
def blizanci():
    znak = 'Blizanci'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-blizanci/',
        'https://www.astroputnik.com/horoskop-za-sutra-blizanci/',
        'https://www.astroputnik.com/nedeljni-horoskop-blizanci/',
        'https://www.astroputnik.com/mesecni-horoskop-blizanci/',
        'https://www.astroputnik.com/godisnji-horoskop-blizanci/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/rak')
def rak():
    znak = 'Rak'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-rak/',
        'https://www.astroputnik.com/horoskop-za-sutra-rak/',
        'https://www.astroputnik.com/nedeljni-horoskop-rak/',
        'https://www.astroputnik.com/mesecni-horoskop-rak/',
        'https://www.astroputnik.com/godisnji-horoskop-rak/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/lav')
def lav():
    znak = 'Lav'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-lav/',
        'https://www.astroputnik.com/horoskop-za-sutra-lav/',
        'https://www.astroputnik.com/nedeljni-horoskop-lav/',
        'https://www.astroputnik.com/mesecni-horoskop-lav/',
        'https://www.astroputnik.com/godisnji-horoskop-lav/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/devica')
def devica():
    znak = 'Devica'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-devica/',
        'https://www.astroputnik.com/horoskop-za-sutra-devica/',
        'https://www.astroputnik.com/nedeljni-horoskop-devica/',
        'https://www.astroputnik.com/mesecni-horoskop-devica/',
        'https://www.astroputnik.com/godisnji-horoskop-devica/'
    ]
    return get_horoscope_data(znak, urls)




@app.route('/vaga')
def vaga():
    znak = 'Vaga'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-vaga/',
        'https://www.astroputnik.com/horoskop-za-sutra-vaga/',
        'https://www.astroputnik.com/nedeljni-horoskop-vaga/',
        'https://www.astroputnik.com/mesecni-horoskop-vaga/',
        'https://www.astroputnik.com/godisnji-horoskop-vaga/'
    ]
    return get_horoscope_data(znak, urls)




@app.route('/skorpija')
def skorpija():
    znak = 'Skorpija'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-skorpija/',
        'https://www.astroputnik.com/horoskop-za-sutra-skorpija/',
        'https://www.astroputnik.com/nedeljni-horoskop-skorpija/',
        'https://www.astroputnik.com/mesecni-horoskop-skorpija/',
        'https://www.astroputnik.com/godisnji-horoskop-skorpija/'
    ]
    return get_horoscope_data(znak, urls)


@app.route('/strelac')
def strelac():
    znak = 'Strelac'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-strelac/',
        'https://www.astroputnik.com/horoskop-za-sutra-strelac/',
        'https://www.astroputnik.com/nedeljni-horoskop-strelac/',
        'https://www.astroputnik.com/mesecni-horoskop-strelac/',
        'https://www.astroputnik.com/godisnji-horoskop-strelac/'
    ]
    return get_horoscope_data(znak, urls)



@app.route('/jarac')
def jarac():
    znak = 'Jarac'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-jarac/',
        'https://www.astroputnik.com/horoskop-za-sutra-jarac/',
        'https://www.astroputnik.com/nedeljni-horoskop-jarac/',
        'https://www.astroputnik.com/mesecni-horoskop-jarac/',
        'https://www.astroputnik.com/godisnji-horoskop-jarac/'
    ]
    return get_horoscope_data(znak, urls)


@app.route('/vodolija')
def vodolija():
    znak = 'Vodolija'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-vodolija/',
        'https://www.astroputnik.com/horoskop-za-sutra-vodolija/',
        'https://www.astroputnik.com/nedeljni-horoskop-vodolija/',
        'https://www.astroputnik.com/mesecni-horoskop-vodolija/',
        'https://www.astroputnik.com/godisnji-horoskop-vodolija/'
    ]
    return get_horoscope_data(znak, urls)


@app.route('/ribe')
def ribe():
    znak = 'Ribe'
    urls = [
        'https://www.astroputnik.com/dnevni-horoskop-ribe/',
        'https://www.astroputnik.com/horoskop-za-sutra-ribe/',
        'https://www.astroputnik.com/nedeljni-horoskop-ribe/',
        'https://www.astroputnik.com/mesecni-horoskop-ribe/',
        'https://www.astroputnik.com/godisnji-horoskop-ribe/'
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
