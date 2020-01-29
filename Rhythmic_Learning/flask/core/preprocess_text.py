import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

import wikipedia
import string
import pyphen
import pronouncing

def clean_page_content(page_content):
    # List containing the first 15 sentences of the page (page summary)
    sentences = sent_tokenize(page_content)[:15]
    # Removed punctuation from all sentences
    cleaned_sentences = [sent.translate(str.maketrans('', '', string.punctuation)) for sent in sentences]
    # Lower case all letters in sentences
    cleaned_sentences = [sent.lower() for sent in cleaned_sentences]

    return cleaned_sentences

def sylabize_all_words(cleaned_sentences):
    dic = pyphen.Pyphen(lang='nl_NL')

    all_sentences = []
    for sent in cleaned_sentences:
        sentence = []
        words = sent.split()
        for word in words:
            sentence.append(dic.inserted(word))
        all_sentences.append(sentence)

    return all_sentences


#
