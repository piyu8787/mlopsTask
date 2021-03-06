# -*- coding: utf-8 -*-
"""dog and cat dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CBTZK-s1UWtsucFQwVf883EEK82FdxUQ
"""

from keras.layers import Convolution2D

from keras.layers import MaxPooling2D

from keras.layers import Flatten

from keras.layers import Dense

from keras.models import Sequential

model = Sequential()

model.add(Convolution2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                   input_shape=(64, 64, 3)
                       ))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.summary()

model.add(Dense(units=128, activation='relu'))

model.summary()

model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'] )

model.summary()

from keras_preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        '/root/filter_dataset/train_cat_dog',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        '/root/filter_dataset/test_cat_dog',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
model.fit(
        training_set,
        steps_per_epoch=1000,
        epochs=3,
        validation_data=test_set,
        validation_steps=500)

