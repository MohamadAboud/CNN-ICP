import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('./cifar10_model.h5')

# List of class names for the CIFAR-10 dataset.
class_names = ['airplane', 'automobile', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


def preprocess_img(img):
    """
    Resize image
    """

    return np.expand_dims(img, axis=0)


def model_predict(image_path):
    img = cv2.imread(image_path)
    img = preprocess_img(img)
    img = img/255.0

    prediction = model.predict(img)
    index = np.argmax(prediction)

    return class_names[index]


# if __name__ == "__main__":
#     image_path = './app/static/uploads/images/bird_75.png'
#     prediction = model_predict(image_path=image_path)
#     print(prediction)
