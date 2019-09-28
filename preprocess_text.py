import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

import wikipedia
import string
import pyphen
import pronouncing

def grab_summaries():
    rand = wikipedia.random(pages=10)
    summary_text_joined = ''
    for page in rand:
        try:
            p = wikipedia.page(page)
        except wikipedia.DisambiguationError as e:
            pass
        summary_text_joined += str(p.summary).lower()

    return summary_text_joined

def grabSummaries():
    rand = wikipedia.random(pages=50)
    summary_text_joined = "" # Variable to store all of the joined summaries
    for search in rand:
        try:
            p = wikipedia.page(search)
        except wikipedia.DisambiguationError as e:
            s = e.options[0] # Selection
            p = wikipedia.page(s)
        summary_text_joined += str(p.content)
    return summary_text_joined
    print("Final:", summary_text_joined) # Testing    

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

def find_rhymes(word, level):
     entries = nltk.corpus.cmudict.entries()
     syllables = [(word, syl) for word, syl in entries if word == word]
     rhymes = []
     for (word, syllable) in syllables:
             rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
     return set(rhymes)


#cleaned_sentences = clean_page_content(page_content)

#hyphened_sentences = sylabize_all_words(cleaned_sentences)

#print(find_rhymes('term', 1))

# Find rhymes of a word
#print(pronouncing.rhymes('bank'))

all_summaries = grab_summaries()

print(clean_page_content(all_summaries))
