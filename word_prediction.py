from numpy import array
import pickle

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# generate a sequence from the model
def generate_seq(model, tokenizer, seed_text, n_words):
	in_text, result = seed_text, seed_text
	# generate a fixed number of words
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

# source text
data = ppt.grabSummaries() #wikipedia.page("List of Marvel Cinematic Universe films").content
print(data)
# data = """ Jack and Jill went up the hill\n
# 		To fetch a pail of water\n
# 		Jack fell down and broke his crown\n
# 		And Jill came tumbling after\n """

# integer encode text
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
encoded = tokenizer.texts_to_sequences([data])[0]
# determine the vocabulary size
print("-->", tokenizer.word_index)
vocab_size = len(tokenizer.word_index) + 1
print('Vocabulary Size: %d' % vocab_size)
# create word -> word sequences
sequences = list()
for i in range(1, len(encoded)):
	sequence = encoded[i-1:i+1]
	sequences.append(sequence)
print('Total Sequences: %d' % len(sequences))
# split into X and y elements
sequences = array(sequences)
X, y = sequences[:,0],sequences[:,1]
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
model.fit(X, y, epochs=100, verbose=2)
# evaluate
print(generate_seq(model, tokenizer, 'superhero', 5))
def reverse_sequence(sequence):
    reversed_sentence = ''
    for word in reversed(sequence.split()):
        reversed_sentence += word + ' '

    return reversed_sentence


sequence = generate_seq(model, tokenizer, 'term', 7)
reversed_sentence = reverse_sequence(sequence)

print(reversed_sentence)
