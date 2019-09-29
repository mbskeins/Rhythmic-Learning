from numpy import array
import pickle

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# generate a sequence from the model
def generate_seq(model, tokenizer, seed_text, n_words):
    in_text, result = seed_text, seed_text
    # generate a fixed number of n_words
    for _ in range(n_words):
        # encode the text as integer
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        encoded = array(encoded)
        # predict a word in the vocabulary
        yhat = model.predict_classes(encoded, verbose=0)
        # map predicted word index to word
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        # append to input
        in_text, result = out_word, result + ' ' + out_word

    return result

def reverse_sequence(sequence):
    reversed_sentence = ''
    for word in reversed(sequence.split()):
        reversed_sentence += word + ' '

    return reversed_sentence

'''
sequence = generate_seq(model, tokenizer, 'honey', 4)
reversed_sentence = reverse_sequence(sequence)

print(reversed_sentence)
'''
