import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

import wikipedia
import string
import re

p = wikipedia.page('Cat')

page_url = p.url
page_title = p.title
page_content = p.content # Content of page

# List containing the first 15 sentences of the page (page summary)
sentences = sent_tokenize(page_content)[:15]

# Removed punctuation from all sentences
cleaned_sentences = [sent.translate(str.maketrans('', '', string.punctuation)) for sent in sentences]

print(cleaned_sentences)
