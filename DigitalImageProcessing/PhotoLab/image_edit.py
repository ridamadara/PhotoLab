import cv2
from PIL import Image


class ImageEditing:
    def __init__(self, img):
        self.original_image = img
        self.edited_image = ""
        self.is_successful = False

    def image_resize(self, height, width):
        original_img = Image.open(self.original_image)
        # image = Image.open('../media/pics/laptop.jpg')
        self.edited_image = original_img.resize((height, width))
        # print(image.size)  # Output: (1920, 1280)
        # print(new_image.size)  # Output: (400, 400)
        self.edited_image.show()
        return self.edited_image
