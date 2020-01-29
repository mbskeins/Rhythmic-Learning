import pronouncing
import wikipedia
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import sys
#import core.word_prediction as wp
import pickle
import random

import importlib.util
spec = importlib.util.spec_from_file_location("word_prediction", "/Users/augmentedmode/Desktop/All-Repos/Hackathon2019/Rhythmic_Learning/flask/core/word_prediction.py")
wp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wp)

with open('/Users/augmentedmode/Desktop/All-Repos/Hackathon2019/Rhythmic_Learning/flask/core/models/model-v5.pkl', 'rb') as f:
    model = pickle.load(f)

with open('/Users/augmentedmode/Desktop/All-Repos/Hackathon2019/Rhythmic_Learning/flask/core/models/tokenizer-v5.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

adlibs = ["Yeee DJ Rhytmic in da house","Learnin makes them earnins","Schoolin n Coolin"]

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
                seq = wp.generate_seq(model, tokenizer, 208-1, rhyme, 6)

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
    return new_list

def print_tuple(tupled_list):
    formatted_list = []
    for item1,item2 in tupled_list:
        formatted_list.append(item1)
        formatted_list.append(item2)
    return formatted_list

def return_tuple_in_list(tupled_list):
    formatted_list = []
    for item1,item2 in tupled_list:
        formatted_list.append(item1)
        formatted_list.append(item2)
    return formatted_list

def formatted_list_output(formatted_list):
    master_list = []
    for line in formatted_list:
        master_list.append(line.split(" "))
    return master_list


def get_final_result(result):
    finallist = [ ", ".join(item.split(" ")) for item in result ]
    '''
    final_result = []
    for sent in finallist:
        final_result.append(sent[:-1])
    '''
    return finallist

def rhyme_it(topic): # Takes a summary and creates a Rhyme for the each line
    try:
        summary = wikipedia.page(topic).summary
    except wikipedia.exceptions.DisambiguationError as e:
        topic = random.choice(e.options)
        summary = wikipedia.page(topic).summary
    lines = clean_page_content(summary)
    words_to_rhyme = get_last_word(lines)
    generated_sentences = []
    for word in words_to_rhyme:
        rhyming_sentence = create_rhyme_sentence(word)
        generated_sentences.append(rhyming_sentence)
    the_rap = combine_sentences(lines,generated_sentences) # Tuple
    the_rap = return_tuple_in_list(the_rap) # List of sentences
    #the_rap = get_final_result(the_rap)
    return the_rap
    #print(formatted_list_output(the_rap)) # List of sentences broken down into words

print('Have not yet started output')
results = rhyme_it(sys.argv[1])

print('[Starting output]')

print(results)

print('[Finished output]')
print("ARG", sys.argv[1])
