from flask import Flask, render_template,request

import tensorflow as tf
import os
import cv2
import keras
import numpy as np

from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.preprocessing.image import load_img
from keras.applications import ResNet50
from keras.applications import InceptionV3
from keras.applications import ResNet50V2
from keras.layers import Dropout
from keras.models import Sequential
from keras.utils import image_dataset_from_directory

app = Flask(__name__)
model = ResNet50()
model2= InceptionV3()
model3= ResNet50V2()

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/', methods=['POST'])

def predict():
    imagefile= request.files['imagefile']
    image_path= "./image/"+imagefile.filename
    imagefile.save(image_path)

    image = load_img(image_path, target_size=(264, 264))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    label = decode_predictions(yhat)
    label = label[0][0]

    classification = '%s (%.2f%%)' % (label[1], label[2] * 100)

    return render_template('index.html', prediction=classification)



if __name__ == '__main__':
    app.run(port=3000, debug=True)
