import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb


word_index=imdb.get_word_index()
reverse_word_index={values:key for key,values in word_index.items()}



model=load_model('imdb_simple_RNN_model.keras')


def preprocess_text(text):
  words=text.lower().split()
  encoded_review=[word_index.get(word,2)+3 for word in words]
  encoded_review=[i if i<10000 else 2 for i in encoded_review]
  padded_review=sequence.pad_sequences([encoded_review], maxlen=500)
  return padded_review


def decode_review(encoded_review):
  return ' '.join([reverse_word_index.get(i-3,'?') for i in encoded_review])


def predict_sentiment(review):

  preprocessed_input = preprocess_text(review)

  prediction=model.predict(preprocessed_input)

  sentiment='Positive' if prediction[0][0]>0.5 else 'Negitive'

  return sentiment,prediction

import streamlit as st

st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negetive')


user_input=st.text_area('Movie Review')

if st.button('Classify'):
  preprocessed_input=preprocess_text(user_input)

  prediction=model.predict(preprocessed_input)

  sentiment='Positive' if prediction[0][0] >0.5 else 'Negative'

  st.write(f'sentiment: {sentiment}')
  st.write(f'Prediction Score: {prediction[0][0]}')

else:
  st.write('Plese enter a movie review')

