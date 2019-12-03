import tensorflow as tf
import random
import numpy as np
import cv2
from PIL import Image
from pathlib import Path
import os
import glob
from tensorflow.keras.preprocessing.image import ImageDataGenerator

label_array = ["1", "2", "3", "4", "5", "a", "e", "i", "o", "u"]
label_to_index = dict((name, index) for index,name in enumerate(label_array))

def getPic(img_path):
  try:
    return np.array(Image.open(img_path).convert('RGB').resize((256,256),Image.ANTIALIAS))
  except:
    print('ERROR on get pic:', img_path)

def get_label(img_path):
  return Path(img_path).absolute().name[0:1]

def get_ds(data_path):
  img_paths = list()

  for label in label_array:
    for img_path in os.listdir(data_path + label):
      img_paths.append(img_path)

    images = np.zeros((len(img_paths),256,256,3))
    labels = np.zeros(len(img_paths))

    # resize the images, get the encoded labels
    for i, img_path in enumerate(img_paths):
      images[i] = getPic(data_path + img_path[:1] + '/' + img_path)
      labels[i] = label_to_index[get_label(data_path + label + '/' + img_path)]

  return images,labels

# Model Architecture
model = tf.keras.Sequential([
  tf.keras.layers.Input(shape=(256,256,3)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(
  optimizer='adam',
  loss='sparse_categorical_crossentropy',
  metrics=['accuracy']
)

train_X, train_y = get_ds("sign-recognition/dataset/train/")

val_X, val_y = get_ds("sign-recognition/dataset/test/")

model.fit(train_X, train_y, validation_data=(val_X, val_y))

model.predict(val_X)

# train_datagen = ImageDataGenerator(
#         rescale=1./255,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True)
#
# test_datagen = ImageDataGenerator(rescale=1./255)
#
# train_generator = train_datagen.flow_from_directory(
#         'dataset/men/',
#         target_size=(150, 150),
#         batch_size=32,
#         class_mode='binary')
#
# validation_generator = test_datagen.flow_from_directory(
#         'dataset/dataset/',
#         target_size=(150, 150),
#         batch_size=32,
#         class_mode='binary')
#
# model.fit_generator(
#         train_generator,
#         steps_per_epoch=2000,
#         epochs=50,
#         validation_data=validation_generator,
#         validation_steps=800)
