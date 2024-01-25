from django.db import models

# Create your models here.
class Prediction(models.Model):

    image = models.ImageField(upload_to="predicted")
    model = models.CharField(max_length=100, choices=[('1', 'Model 1 - InceptionV3'),
                                                      ('2',
                                                       'Model 2 -  ResNet50V1 Dropout'),
                                                      ('3', 'Model 3 - ResNet50V1 Sequential Model'),
                                                      ('4',
                                                       'Model 4 - ResNet50V2 Dropout'),
                                                      ('5',
                                                       'Model 5 - ResNet50V2 Sequential Model')])

    predicted_value = models.CharField(max_length=10)
    likelihood_indoor = models.FloatField()
    likelihood_outdoor = models.FloatField()
