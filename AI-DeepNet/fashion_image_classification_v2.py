# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vl0giA7XqKycq9xtpEh3HsUoiWTZSjaS
"""

from tensorflow.keras.models import load_model
from tensorflow.keras import utils
from tensorflow.keras.preprocessing import image
import numpy as np
from IPython.display import Image
from google.colab import files

classes = ['футболка', 'брюки', 'свитер', 'платье', 'пальто', 'туфли', 'рубашка', 'кроссовки', 'сумка', 'ботинки']

model = load_model('fashion_mnist_dense.h5')
model.summary()

img_path = 'sweater.jpg'
Image(img_path, width=150, height=150)

img = image.load_img(img_path, target_size=(28, 28), color_mode = "grayscale")

x = image.img_to_array(img)
x = x.reshape(1, 784)
x = 255 - x
x /= 255

prediction = model.predict(x)
prediction = np.argmax(prediction)
print('Номер класса: ',  prediction)
print('Название класса: ', classes[prediction])