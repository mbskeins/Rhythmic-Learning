from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding

import preprocess_text as preprocess

import pickle


# source text
import wikipedia
p = wikipedia.page('money')

page_url = p.url
page_title = p.title
page_content = p.content # Content of page
data = preprocess.clean_page_content(page_content)
data = ''.join(data)


# integer encode text
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
encoded = tokenizer.texts_to_sequences([data])[0]
# determine the vocabulary size
vocab_size = len(tokenizer.word_index) + 1
print('Vocabulary Size: %d' % vocab_size)
# create word -> word sequences
sequences = list()
for i in range(1, len(encoded)):
	sequence = encoded[i-1:i+1]
	sequences.append(sequence)
print('Total Sequences: %d' % len(sequences))
# split into X and y elements

# Reverse the sequences to predict the previous word
reversed_sequences = []
for seq in sequences:
    seq[0], seq[1] = seq[1], seq[0]
    reversed_sequences.append(seq)

reversed_sequences = array(reversed_sequences)
X, y = reversed_sequences[:,0],reversed_sequences[:,1]
# one hot encode outputs
y = to_categorical(y, num_classes=vocab_size)
# define model
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=1))
model.add(LSTM(50))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
# compile network
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit network
model.fit(X, y, epochs=200, verbose=2)

# Pickle the model and the tokenizer
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('models/tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)
