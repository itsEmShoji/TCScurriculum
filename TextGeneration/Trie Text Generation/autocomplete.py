import nltk
import numpy as np
import random
import string

import bs4 as bs
import urllib.request
import re

from Trie import *

# pre-proceessing
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

# Insert words into Trie
trie = Trie()

for word in article_text.split():
    trie.add(word)

# generate text
# have not determined an effective way to generate a paragraph of text

print("'goodbye' in trie: ", trie.has_word('goodbye'))
print(trie.start_with_prefix('i'))
print(trie.start_with_prefix('t'))
