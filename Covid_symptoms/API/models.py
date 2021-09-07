from django.db import models

# Create your models here.
"""
class predictor(models.Model):
    Cough_choice= (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Fever_choice= (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Throat_choice= (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Breathing= (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Headache= (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Above60= (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Gender_choice= (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    Situation= (
        ('Contact', 'Contact'),
        ('Abroad', 'Abroad'),
        ('Other', 'Other')
    )
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    cough= models.CharField(max_length=15, choices=Cough_choice)
    fever= models.CharField(max_length=15, choices=Fever_choice)
    throat= models.CharField(max_length=15, choices=Throat_choice)
    breathe= models.CharField(max_length=15, choices=Breathing)
    ha= models.CharField(max_length=15, choices=Headache)
    senior= models.CharField(max_length=15, choices=Above60)
    gender= models.CharField(max_length=15, choices=Gender_choice)
    sit= models.CharField(max_length=15, choices=Situation)
    def __str__(self):
        return '{}, {}'.format(self.lastname, self.firstname)


"""