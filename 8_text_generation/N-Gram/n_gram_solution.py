import nltk
import random
import string

import bs4 as bs
import urllib.request
import re

# preprocessing
raw_html = urllib.request.urlopen(
    'https://www.site.uottawa.ca/~lucia/courses/2131-02/A2/trythemsource.txt')
raw_html = raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')
article_paragraphs = article_html.find_all('p')
article_text = ''

for para in article_paragraphs:
    article_text += para.text

article_text = article_text.lower()

article_text = article_text.translate(
    str.maketrans('', '', string.punctuation))

# create model
ngrams = {}
chars = 4

for i in range(len(article_text)-chars):
    seq = article_text[i:i+chars]
    print(seq)
    if seq not in ngrams.keys():
        ngrams[seq] = []
    ngrams[seq].append(article_text[i+chars])


# generate text
curr_sequence = article_text[0:chars]
output = curr_sequence
for i in range(200):
    if curr_sequence not in ngrams.keys():
        break
    possible_chars = ngrams[curr_sequence]
    next_char = possible_chars[random.randrange(len(possible_chars))]
    output += next_char
    curr_sequence = output[len(output)-chars:len(output)]

print(output)


# Installations:
# pip install --user -U nltk
# pip install --user -U numpy
# pip install beautifulsoup4
# /Applications/Python\ 3.6/Install\ Certificates.command
# pip install lxml
