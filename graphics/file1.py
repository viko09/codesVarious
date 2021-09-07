import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as k

k.clear_session()

data_train = './data/training'
data_val = './data/validation'

# Epocas

epocas = 20
altura, longitud = 100, 100
batch_size = 32
steps = 1000

validation_Steps = 200

filters_conv1 = 32
filters_conv2 = 64

filter_size1 = (3, 2)
filter_size2 = (2, 2)
size_pool = (2, 2)
classes = 3
lr = 0.0005

# procesar imagenes

training_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True
)

validation_datagen = ImageDataGenerator(
    rescale=1./255
)

pic_training = training_datagen.flow_from_directory(
    data_train,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)

pic_validation = validation_datagen.flow_from_directory(
    data_val,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)

# Crear la red

cnn = Sequential()
cnn.add(Convolution2D(filters_conv1, filter_size1, padding='same', input_shape=(altura, longitud), activation='relu'))
cnn.add(MaxPooling2D(pool_size=size_pool))
cnn.add(Convolution2D(filters_conv2, filter_size2, padding='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size=size_pool))

cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(classes, activation='softmax'))

cnn.compile(loss='categorical_crossentropy', optimizer=optimizers.Adam(lr=lr), metrics=['accuracy'])

cnn.fit(pic_training, steps_per_epoch=steps, epochs=epocas, validation_steps=validation_Steps)
