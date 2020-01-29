import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

import wikipedia
import string
import pyphen
import pronouncing
import re

import pickle

def grab_summaries():
    rand = wikipedia.random(pages=50)
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
    cleaned_summaries = ''
    words = set(nltk.corpus.words.words())
    all_summaries = nltk.sent_tokenize(all_summaries)


    for sent in all_summaries:

        sent = sent.translate(str.maketrans('', '', string.punctuation))

        sent = sent.replace('°', '').replace('-', '').replace(" ' ", '')

        sent = re.sub(r"[\(\[].*?[\)\]]", "", sent)

        sent = ''.join([i for i in sent if not i.isdigit()])

        sent = ' '.join(w for w in nltk.wordpunct_tokenize(sent) if w.lower() in words or not w.isalpha())

        sent += ' + '

        cleaned_summaries += sent



    return cleaned_summaries

big_summary = ''

for i in range(10):
    print('starting grab')
    all_summaries = grab_summaries()

    big_summary += all_summaries
    print('got big summary')


cleaned_summaries = clean_text(big_summary)
print('finished!')



with open('corpuses/split_lines_corp1.pkl', 'wb') as f:
    pickle.dump(cleaned_summaries, f)
