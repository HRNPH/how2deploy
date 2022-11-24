# Model
from tensorflow.keras.models import load_model
import numpy as np
# tokenizer
import pickle
import pythainlp as pythai
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# load model
model = load_model('./model/weight/model.h5')
# load tokenizer
with open('./model/weight/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def predict(text, decode=False):
    text = pythai.word_tokenize(text, engine='newmm')
    text = tokenizer.texts_to_sequences([text])
    text = pad_sequences(text, maxlen=60, padding='post', truncating='post')
    predict = model.predict(text)
    rounded = np.round(predict)
    if decode:
        return 'pos' if rounded == 1 else 'neg'
    return rounded