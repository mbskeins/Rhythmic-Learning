from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras.callbacks import ModelCheckpoint

import pickle
import time

with open('corpuses/main_corpus.pkl', 'rb') as f:
    data = pickle.load(f)

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

checkpoint = ModelCheckpoint(f'checkpoint{time.time()}.hdf5', monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=12)
callbacks_list = [checkpoint]
# fit network
model.fit(X, y, epochs=6, verbose=1, callbacks=callbacks_list)


# Pickle the model and the tokenizer
with open('models/model-v5.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('models/tokenizer-v5.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)
