from numpy import array
from keras.preprocessing.sequence import pad_sequences

import pickle

with open('models/model-v5.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/tokenizer-v5.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# generate a sequence from a language model
def generate_seq(model, tokenizer, max_length, seed_text, n_words):
    in_text = seed_text
    all_yhat = []
    # generate a fixed number of words
    for _ in range(n_words):
	    # encode the text as integer
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        print(encoded)
        # pre-pad sequences to a fixed length
        encoded = pad_sequences([encoded], maxlen=max_length, padding='pre')
        # predict probabilities for each word
        yhat = model.predict_classes(encoded, verbose=0)

        # predict a word in the vocabulary
        temp = model.predict(encoded, verbose=0)
        temp2 = []
        for ind, pred in enumerate(temp[0]):
            temp2.append((pred, ind))
        sorted_by_second = sorted(temp2, reverse=True, key=lambda tup: tup[0])[:10]
        print(sorted_by_second)

        for count, i in enumerate(sorted_by_second):
            if i[1] == 3 or i[1] == 14 or i[1] == 35 or i[1] == 455 or i[1] == 1 or i[1] == 19:
                print(count)
                del sorted_by_second[count]

        from random import randrange
        random_number = randrange(2)
        selected = sorted_by_second[random_number]
        yhat = selected[1]

        if yhat in all_yhat:
            random_number = randrange(4)
            selected = sorted_by_second[random_number]
            yhat = selected[1]


        all_yhat.append(yhat)

        # map predicted word index to word
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        # append to input
        in_text += ' ' + out_word #the_word
    return in_text



def reverse_sequence(sequence):
    reversed_sentence = ''
    for word in reversed(sequence.split()):
        reversed_sentence += word + ' '

    return reversed_sentence
