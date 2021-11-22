from urllib.request import urlopen
from bs4 import BeautifulSoup
import nltk
import re

def html2freq(url):
    page = urlopen(url)
    html = BeautifulSoup(page.read(), 'html.parser')
    s = html.get_text('\n', strip=True)
    s = s.replace('\n', ' ')
    s = re.sub(' +', ' ', s)
    tokens = nltk.word_tokenize(s, language='portuguese')
    return nltk.FreqDist(tokens)

def test():
    url = 'https://pt.wikipedia.org/wiki/Python'
    return html2freq(url)