import keras as keras
import numpy as np
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpRequest
from django.shortcuts import render, redirect

# from demoapp.forms import PredictionForm
# from demoapp.models import Prediction
from .forms import PredictionForm
from .models import Prediction


import os
import cv2


def predict_image(model_number, path, size_x: int = 224, size_y: int = 224):
    print(os. getcwd())
    img = cv2.imread(path[1:])
    print(img)
    img = cv2.resize(img, (size_x, size_y))
    img = np.expand_dims(img, axis=0)
    model = keras.models.load_model(f'demoapp/models/model{model_number}.h5')
    return model.predict(img, verbose=False)[0]


def predict(request: HttpRequest):
    context = dict()
    context["form"] = PredictionForm

    if request.method == "POST":
        form_data = PredictionForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            prediction: Prediction = form_data.save(commit=False)
            prediction.image = form_data.cleaned_data["image"]
            prediction.likelihood_indoor = 0
            prediction.likelihood_outdoor = 0
            prediction.predicted_value = 'none'
            prediction.save()

            probabilities = predict_image(prediction.model, prediction.image.url)

            prediction.likelihood_indoor = probabilities[0]
            prediction.likelihood_outdoor = 1 - probabilities[0]  # Assuming binary classification

            if probabilities[0] >= 0.5:
                prediction.predicted_value = 'outdoor'
            else:
                prediction.predicted_value = 'indoor'

            prediction.save()
            return redirect(f"?image={prediction.image.url}&class={prediction.predicted_value}&likelihood={probabilities[0]}&model={prediction.model}")
    
    return render(request, "prediction.html", context=context)