import nltk
import numpy as np
import random
import string
import lxml
import bs4 as bs
import urllib.request
import re

# preprocessing
raw_html = urllib.request.urlopen(
    'https://www.clear.rice.edu/comp200/resources/texts/Green%20Eggs%20and%20Ham.txt')
raw_html = raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')
article_paragraphs = article_html.find_all('p')
# add code here

# add code here
# add code here

article_text = article_text.translate(
    str.maketrans('', '', string.punctuation))
# add code here

# create model
# add code here
# add code here

# add code here
# add code here
# print(seq)
# add code here
# add code here
# add code here

# generate text
# add code here
# add code here
# add code here:
# add code here
# add code here
# add code here
next_char = possible_chars[random.randrange(len(possible_chars))]
# add code here
# add code here

# add code here
