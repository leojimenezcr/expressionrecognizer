import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_image_segmented_image(image, clusters = 5):
  image = cv2.imread(image)

  # convert to RGB, all the images
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  # reshape the image to a 2D array of pixels and 3 color values (RGB)
  pixel_values = image.reshape((-1, 3))

  # convert to float
  pixel_values = np.float32(pixel_values)

  # define stopping criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

  compactness, labels, (centers) = cv2.kmeans(pixel_values, clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

  # convert back to 8 bit values
  centers = np.uint8(centers)

  # convert all pixels to the color of the centroids
  segmented_image = centers[labels.flatten()]

  # reshape back to the original image dimension
  segmented_image = segmented_image.reshape(image.shape)

  return segmented_image

def show_segmented_image(image):
  plt.imshow(image)
  plt.show()
