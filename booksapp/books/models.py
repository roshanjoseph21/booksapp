from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    # year=models.PositiveIntegerField
    genre=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    # price=models.PositiveIntegerField

    def __str__(self):
        return self.name


    # Book.objects.create(name="The GreatGatsby",author="F. Scott Fitzgerald",genre="Literature",rating="4.5")
    #Book.objects.create(name="Alice's Adventures in Wonderland",author="Lewis Carroll",genre="Story",rating="4.5")
    #Nineteen Eighty-Four