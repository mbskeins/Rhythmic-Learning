import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

import wikipedia
import string
import pyphen
import pronouncing
import re

import pickle

def grab_summaries():
    rand = wikipedia.random(pages=10000)
    summary_text_joined = ''
    for page in rand:
        try:
            p = wikipedia.page(page)
        except wikipedia.DisambiguationError as e:
            p = ''
            pass
        except wikipedia.exceptions.PageError as e:
            p = ''
            pass

        if p != '':
            summary_text_joined += str(p.summary).lower()

    return summary_text_joined


def clean_text(all_summaries):
    words = set(nltk.corpus.words.words())

    all_summaries = all_summaries.translate(str.maketrans('', '', string.punctuation))

    all_summaries = all_summaries.replace('°', '').replace('-', '').replace(" ' ", '')

    all_summaries = re.sub(r"[\(\[].*?[\)\]]", "", all_summaries)

    all_summaries = ''.join([i for i in all_summaries if not i.isdigit()])

    all_summaries = ' '.join(w for w in nltk.wordpunct_tokenize(all_summaries) \
                     if w.lower() in words or not w.isalpha())

    return all_summaries

big_summary = ''

for i in range(6):

    all_summaries = grab_summaries()

    big_summary += all_summaries

cleaned_summaries = clean_text(big_summary)

with open('corpuses/largest-corpus.pkl', 'wb') as f:
    pickle.dump(cleaned_summaries, f)
