import streamlit as st
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# código omitido


def carregar_modelo():
    url = 'modelo_vidente.keras'
    loaded_model = tf.keras.load_model('model_vidente.keras')

    with open('vectorized.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

    return loaded_model, vectorizer

def predict_next_words(model, vectorizer, text, max_sequence_len, top_k=3):
    tokenized_text = vectorizer([text])
    tokenized_text = np.squeeze(tokenized_text)

    padded_text = pad_sequences([tokenized_text], maxlen=max_sequence_len, padding='pre')

    predicted_probs = model.predict(padded_text, verbose=0)[0]

    top_k_indices = np.argsort(predicted_probs)[-top_k:][::-1]

    predicted_words = [vectorizer.get_vocabulary()[index] for index in top_k_indices]

    return predicted_words


def main():

    max_sequence_len = 50

    loaded_model, vectorizer = carregar_modelo()

    st.title('Previsão de Próximas Palavras')

    input_text = st.text_input('Digite uma sequência de texto:')

    if st.button('Prever')

if __name__ == "__main__":
     main()
