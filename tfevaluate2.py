from keras_preprocessing.text import tokenizer_from_json
from numpy.core.fromnumeric import squeeze
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os


import pandas as pd
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences



vocab_size = 10000
embedding_dim=30
max_length=5
training_size = 30000


columnNames=["headline","clickbait"]
df = pd.read_csv('/Users/rickzhang/Documents/code/htn/google/hack-the-north-2021/api/clickbait_data.csv')

inputTitles= df.headline.to_list()
clickbait = df.clickbait.to_list()


training_sentences = inputTitles[0:training_size]
testing_sentences = inputTitles[training_size:]
training_clickbait = clickbait[0:training_size]
testing_clickbait = clickbait[training_size:]



tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")

tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index


training_sequences = tokenizer.texts_to_sequences(training_sentences)
training_padded = pad_sequences(training_sequences, maxlen=max_length,padding='post',truncating='post')



testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequences,maxlen=max_length,padding='post',truncating='post')


training_padded = np.array(training_padded)
training_labels = np.array(training_clickbait)
testing_padded = np.array(testing_padded)
testing_labels = np.array(testing_clickbait)




# model = tf.keras.Sequential(tf.keras.layers.Embedding(vocab_size,embedding_dim,input_length=max_length))
# model.add(tf.keras.layers.Convolution1D(32,2))

# model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.Activation('relu'))
# model.add(tf.keras.layers.Convolution1D(32,2))
# model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.Activation('relu'))
# model.add(tf.keras.layers.Flatten())
# model.add(tf.keras.layers.Dense(1))
# model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.Activation('sigmoid'))

# model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
# model.summary()

# num_epochs = 20
# history = model.fit(x=np.array(training_padded),y=np.array(training_clickbait),shuffle=True,epochs=num_epochs,validation_data=(np.array(testing_padded),np.array(testing_clickbait)),verbose=2)

# model.save('tfmodels')

# def plot_graphs(history,string):
#     plt.plot(history.history[string])
#     plt.plot(history.history['val_'+string])
#     plt.xlabel("Epochs")
#     plt.ylabel(string)
#     plt.legend([string, 'val_'+string])
#     plt.show()
  
# plot_graphs(history, "accuracy")
# plot_graphs(history, "loss")

new_model = tf.keras.models.load_model('tfmodels')
new_model.summary()
model = new_model


def main(text):
    
    mySequence = tokenizer.texts_to_sequences(text)
    mySeqPadded = pad_sequences(mySequence,maxlen=max_length,padding='post',truncating='post')
    print(model.predict(mySeqPadded)[0,0])
    ans= model.predict(mySeqPadded)
    return ("{:0.2f}".format(ans*100))


# main('hello world i am buying a car')
