#CAPTAR DATA EM TEMPO REAL
from requests import get
from bs4 import BeautifulSoup as bs
import html5lib

h = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 OPR/85.0.4341.18'}

url = get('https://www.wikidates.org/br/data-de-hoje.html', headers=h)
page = bs(url.content, 'html5lib')
d = page.find('p')
dia = d.text

diat = dia.replace('• A data de hoje: ', '')
diafinal = diat.replace('.', '')

diaa = page.find(id="dmenudate")
dias = diaa.text
diasemana = dias.replace(', 29 março 2022 (Semana: 13)', '')