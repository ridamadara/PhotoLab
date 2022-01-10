from deepface import DeepFace


def image_recognition(img):
    r = DeepFace.verify(img, img)
    return r
# r = DeepFace.verify("../media/pics/hamdan.jpeg", "../media/pics/hamdan.jpeg")
# print(r)