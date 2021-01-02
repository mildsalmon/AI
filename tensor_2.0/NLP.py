from tensorflow.keras.preprocessing.text import text_to_word_sequence

text='해보지 않으면 해낼 수 없다'
result = text_to_word_sequence(text)
print(result)

from tensorflow.keras.preprocessing.text import Tokenizer

docs = ['먼저 텍스트의 각 단어를 나누어 토큰화 합니다.',
       '텍스트의 단어로 토큰화 해야 딥러닝에서 인식됩니다.',
       '토큰화 한 결과는 딥러닝에서 사용 할 수 있습니다.',
       ]

token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_counts)
print(token.document_count)
print(token.word_docs)
print(token.word_index)

from tensorflow.keras.preprocessing.text import Tokenizer

text = "오랫동안 꿈꾸는 이는 그 꿈을 닮아간다"

token = Tokenizer()
token.fit_on_texts([text])
print(token.word_index)

print("\n")

x = token.texts_to_sequences([text])
print(x)

from keras.utils import to_categorical

word_size = len(token.word_index) + 1
x = to_categorical(x, num_classes=word_size)

print(x)

import numpy
import tensorflow as tf
from numpy import array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten,Embedding

from keras.layers import Embedding

model = Sequential()
model.add(Embedding(16, 4))

padded_x = pad_sequences(x, 4)