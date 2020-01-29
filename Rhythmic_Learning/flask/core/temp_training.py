from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
from keras.callbacks import ModelCheckpoint

import pickle

# generate a sequence from a language model
def generate_seq(model, tokenizer, max_length, seed_text, n_words):
	in_text = seed_text
	# generate a fixed number of words
	for _ in range(n_words):
		# encode the text as integer
		encoded = tokenizer.texts_to_sequences([in_text])[0]
		# pre-pad sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=max_length, padding='pre')
		# predict probabilities for each word
		yhat = model.predict_classes(encoded, verbose=0)
		# map predicted word index to word
		out_word = ''
		for word, index in tokenizer.word_index.items():
			if index == yhat:
				out_word = word
				break
		# append to input
		in_text += ' ' + out_word
	return in_text


with open('corpuses/split_lines_corp1.pkl', 'rb') as f:
    data = pickle.load(f)

with open('corpuses/split_lines_corp1-1.pkl', 'rb') as f:
    data1 = pickle.load(f)


with open('corpuses/split_lines_corp21569737754.315756.pkl', 'rb') as f:
    data2 = pickle.load(f)

with open('corpuses/split_lines_corp2-1.pkl', 'rb') as f:
    data3 = pickle.load(f)


with open('corpuses/split_lines_corp21569738727.8629088.pkl', 'rb') as f:
    data4 = pickle.load(f)


with open('corpuses/split_lines_corp21569738813.083144.pkl', 'rb') as f:
    data5 = pickle.load(f)

with open('corpuses/split_lines_corp21569742324.0013618.pkl', 'rb') as f:
    data6 = pickle.load(f)


data = data + data1 + data2 + data3 + data4 + data5 + data6



# prepare the tokenizer on the source text
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
# determine the vocabulary size
vocab_size = len(tokenizer.word_index) + 1
print('Vocabulary Size: %d' % vocab_size)
# create line-based sequences
sequences = list()
for line in data.split(' + '):
	encoded = tokenizer.texts_to_sequences([line])[0]
	for i in range(1, len(encoded)):
		sequence = encoded[:i+1]
		sequences.append(sequence)
print('Total Sequences: %d' % len(sequences))

# Reverse the sequences to predict the previous word
def reverse(lst):
    return [ele for ele in reversed(lst)]

reversed_sequences = []
for seq in sequences:
    seq = reverse(seq)
    reversed_sequences.append(seq)

# pad input sequences
max_length = max([len(seq) for seq in reversed_sequences])
print(f'MAXLEN {max_length}')
reversed_sequences = pad_sequences(reversed_sequences, maxlen=max_length, padding='pre')
print('Max Sequence Length: %d' % max_length)
# split into input and output elements
reversed_sequences = array(reversed_sequences)
X, y = reversed_sequences[:,:-1],reversed_sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)
# define model
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_length-1))
model.add(LSTM(50))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
# compile network
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

import time


checkpoint = ModelCheckpoint(f'checkpoint{time.time()}.hdf5', monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=12)
callbacks_list = [checkpoint]
# fit network
model.fit(X, y, epochs=6, verbose=1, callbacks=callbacks_list)


# Pickle the model and the tokenizer
with open('models/new-new-newest-model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('models/new-new-newest-tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

# evaluate model
print(generate_seq(model, tokenizer, max_length-1, 'term', 4))


def reverse_sequence(sequence):
    reversed_sentence = ''
    for word in reversed(sequence.split()):
        reversed_sentence += word + ' '

    return reversed_sentence


sequence = generate_seq(model, tokenizer, max_length-1, 'dash', 6)
reversed_sentence = reverse_sequence(sequence)

print(reversed_sentence)
