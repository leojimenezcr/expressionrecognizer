import tensorflow as tf
import random
import numpy as np
import cv2
from PIL import Image
from pathlib import Path
import os
import glob
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from preprocessing.kmeans_segmentation import get_image_segmented_image

label_array = ["1", "2", "3", "4", "5", "a", "e", "i", "o", "u"]
label_to_index = dict((name, index) for index,name in enumerate(label_array))

dimension = 100

def getPic(img_path):
  try:
  # segmented_image = get_image_segmented_image(img_path)
    image = Image.open(img_path).convert('RGB').resize((dimension,dimension),Image.ANTIALIAS)
    return np.array(image)
  except:
    print('ERROR on get pic:', img_path)

def get_label(img_path):
  return Path(img_path).absolute().name[0:1]

def get_ds(data_path):
  img_paths = list()

  for label in label_array:
    for img_path in os.listdir(data_path + label):
      img_paths.append(img_path)

    images = np.zeros((len(img_paths),dimension,dimension,3))
    labels = np.zeros(len(img_paths))

    # resize the images, get the encoded labels
    for i, img_path in enumerate(img_paths):
      images[i] = getPic(data_path + img_path[:1] + '/' + img_path)
      labels[i] = label_to_index[get_label(data_path + label + '/' + img_path)]

  return images,labels

def run_the_net():
  model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(dimension,dimension,3)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
  ])

  model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
  )

  train_X, train_y = get_ds("signrecognition/dataset/train/")

  val_X, val_y = get_ds("signrecognition/dataset/test/")

  model.fit(train_X, train_y, validation_data=(val_X, val_y))

  model.predict(val_X)
