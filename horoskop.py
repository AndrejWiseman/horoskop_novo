import concurrent.futures
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

def fetch_horoscope(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    return soup.find('div', class_='article-details').text

def blizanci():
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/blizanci/',
        'http://www.horoskopius.com/nedeljni-horoskop/blizanci/',
        'http://www.horoskopius.com/mesecni-horoskop/blizanci/',
        'http://www.horoskopius.com/godisnji-horoskop/blizanci/'
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(fetch_horoscope, urls)

    dnevni, nedeljni, mesecni, godisnji = results

    return render_template('blizanci.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)



def vodolija():
    urls = [
        'http://www.horoskopius.com/dnevni-horoskop/vodolija/',
        'http://www.horoskopius.com/nedeljni-horoskop/vodolija/',
        'http://www.horoskopius.com/mesecni-horoskop/vodolija/',
        'http://www.horoskopius.com/godisnji-horoskop/vodolija/'
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(fetch_horoscope, urls)

    dnevni, nedeljni, mesecni, godisnji = results

    return render_template('vodolija.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)











# from flask import Flask, render_template
# from bs4 import BeautifulSoup
# import requests
#
#
# def blizanci():
#     source = requests.get('http://www.horoskopius.com/dnevni-horoskop/blizanci/').text
#     source_n = requests.get('http://www.horoskopius.com/nedeljni-horoskop/blizanci/').text
#     source_m = requests.get('http://www.horoskopius.com/mesecni-horoskop/blizanci/').text
#     source_g = requests.get('http://www.horoskopius.com/godisnji-horoskop/blizanci/').text
#
#     soup = BeautifulSoup(source, 'lxml')
#     soup_n = BeautifulSoup(source_n, 'lxml')
#     soup_m = BeautifulSoup(source_m, 'lxml')
#     soup_g = BeautifulSoup(source_g, 'lxml')
#
#     dnevni = soup.find('div', class_='article-details').text
#     nedeljni = soup_n.find('div', class_='article-details').text
#     mesecni = soup_m.find('div', class_='article-details').text
#     godisnji = soup_g.find('div', class_='article-details').text
#
#     return render_template('vodolija.html', dnevni=dnevni, nedeljni=nedeljni, mesecni=mesecni, godisnji=godisnji)
#
#
#
