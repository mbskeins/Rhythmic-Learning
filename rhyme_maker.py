import pronouncing
import wikipedia
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import word_prediction as wp
import pickle
import random

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

adlibs = ["Yeee DJ Rhytmic in da house","Learnin makes them earnins","Schoolin n Coolin"]

summary = wikipedia.page("Money").summary
last_word_list = [] # Array of last words of each sentence in order

def clean_page_content(page_content):
    # List containing the first 15 sentences of the page (page summary)
    sentences = sent_tokenize(page_content)[:15]
    # Removed punctuation from all sentences
    cleaned_sentences = [sent.translate(str.maketrans('', '', string.punctuation)) for sent in sentences]
    # Lower case all letters in sentences
    cleaned_sentences = [sent.lower() for sent in cleaned_sentences]

    return cleaned_sentences

def grab_random_adlib():
    return random.choice(adlibs)

def get_last_word(lines):
    for line in lines:
        words = line.split(" ")
        last_word_list.append(words[-1])
    return last_word_list

def find_rhyme_word(word):
    return pronouncing.rhymes(word)

def create_rhyme_sentence(word):
    rhymables = find_rhyme_word(word)
    if len(rhymables) < 1:
        return grab_random_adlib()
    else:
        for rhyme in rhymables:
            try:
                #print(word,"-->",rhyme)
                seq = wp.generate_seq(model, tokenizer, rhyme, 7)
                reversed_sentence = wp.reverse_sequence(seq)
                return reversed_sentence
                break
            except:
                if rhymables[-1] == rhyme:
                    return grab_random_adlib()
                else:
                    pass

def combine_sentences(list1,list2): # Combines two sentences in order
    new_list = zip(list1,list2)
    
    for item1,item2 in new_list:
        print('\n')
        print(item1)
        print(item2)
        print('\n')
    return new_list

def rhyme_it(summary): # Takes a summary and creates a Rhyme for the each line
    print(summary)
    lines = clean_page_content(summary)
    words_to_rhyme = get_last_word(lines)
    generated_sentences = []
    for word in words_to_rhyme:
        rhyming_sentence = create_rhyme_sentence(word)
        generated_sentences.append(rhyming_sentence)
    the_rap = combine_sentences(lines,generated_sentences)


print('\n\n',rhyme_it(summary),'\n\n')
