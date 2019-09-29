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

adlibs = ["Yeee DJ Rhytmic in da house","Learnin makes them earnins","Schoolin n Coolin"] # set of adlibs you can add to

summary = wikipedia.page('facebook').summary
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

# returns list of last words of each sentence
def get_last_word(lines):
    for line in lines:
        words = line.split(" ")
        last_word_list.append(words[-1])

    return last_word_list

def find_rhyme_word(word):
    return pronouncing.rhymes(word)

def create_rhyme_sentence(word):
    # rhymables is the list of words that rhymes with the given word
    rhymables = find_rhyme_word(word)
    if len(rhymables) < 1:
        # random adlib if no rhymable words
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

# Combines two sentences in order
def combine_sentences(list1,list2):
    new_list = zip(list1,list2)

    return new_list

def print_tuple(tupled_list):
    formatted_list = []
    for item1,item2 in tupled_list:
        print(item1)
        formatted_list.append(item1)
        print(item2)
        formatted_list.append(item2)
        print('\n')

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

# Takes a summary and creates a Rhyme for the each line of the summary
def rhyme_it(summary):
    print("Summary:",summary)
    lines = clean_page_content(summary)
    words_to_rhyme = get_last_word(lines)
    generated_sentences = []
    for word in words_to_rhyme:
        rhyming_sentence = create_rhyme_sentence(word)
        generated_sentences.append(rhyming_sentence)
    the_rap = combine_sentences(lines,generated_sentences) # Tuple
    the_rap = return_tuple_in_list(the_rap) # List of sentences

    # List of sentences broken down into words
    # Example Usage:
    # the_rap = formatted_list_output(the_rap)

    return the_rap


result = rhyme_it(summary)

for sent in result:
    print()
    print(sent)
    print()
