import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
import time
from datetime import datetime

start_time = time.time()
print("Start time:", datetime.fromtimestamp(start_time).strftime('%d:%m:%Y %H:%M:%S'))

# load the data into a pandas dataframe
df = pd.read_table('../data/random_samples_new.txt')

# extract the DNA sequences and labels from the dataframe
sequences = df['sequence'].values
labels = df['label'].values

# create a k-mer tokenizer for the sequences
k = 3
tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts(sequences)

# convert the sequences to k-mer encoded sequences
encoded_sequences = tokenizer.texts_to_sequences(sequences)

# pad the encoded sequences to ensure they have the same length
max_length = max([len(x) for x in encoded_sequences])
padded_sequences = pad_sequences(encoded_sequences, maxlen=max_length, padding='post')

# one-hot encode the padded sequences
one_hot_sequences = np.array([np.eye(len(tokenizer.word_index) + 1)[x] for x in padded_sequences])

# split the data into training and testing sets
train_data = one_hot_sequences[:int(0.8 * len(one_hot_sequences))]
train_labels = labels[:int(0.8 * len(labels))]
test_data = one_hot_sequences[int(0.8 * len(one_hot_sequences)):]
test_labels = labels[int(0.8 * len(labels)):]

# create the LSTM model
model = Sequential()
model.add(LSTM(100, input_shape=(max_length, len(tokenizer.word_index) + 1)))
model.add(Dense(5, activation='softmax'))

# compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the model to the training data
model.fit(train_data, train_labels, epochs=50, batch_size=32)

# evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_data, test_labels)
print('Test Accuracy:', test_acc)

start_time = time.time()
print("End time:", datetime.fromtimestamp(start_time).strftime('%d:%m:%Y %H:%M:%S'))