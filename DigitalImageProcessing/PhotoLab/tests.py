from django.test import TestCase
import os
from PIL import Image
# from deepface import DeepFace
from deepface import DeepFace
# Create your tests here.
# img = Image.open('../media/pics/laptop.jpg')
# print(type(img))
# # img.show()
from datetime import datetime


class Comment:
    def __init__(self, email, content, img, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
        self.image = 'laptop.jpg'

class ImageResizer:
    def __init__(self, image):
        self.image = image


# import cv2
# import numpy as np
# from PIL import Image
#
# img = Image.open('../media/pics/dull_img2.jpg')
# image = np.array(img)
#
# # image = cv2.read('../media/pics/text.jpg')
# print(image)
#
# new_image = np.zeros(image.shape, image.dtype)
# alpha = 0.0 # Simple contrast control
# beta = 10    # Simple brightness
#
# result = cv2.addWeighted(image,alpha,new_image,0,beta)
# cv2.imwrite('thisistest2.jpg',image)


# for y in range(image.shape[0]):
#     for x in range(image.shape[1]):
#         for c in range(image.shape[2]):
#             new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
# cv2.imshow('Original Image', image)
# cv2.imshow('New Image', new_image)
# # Wait until user press some key
# cv2.waitKey()





