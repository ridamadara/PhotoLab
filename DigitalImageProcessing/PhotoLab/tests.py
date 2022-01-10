from django.test import TestCase
import os
from PIL import Image
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




