from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name
    

class DailySpecial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='specials/')

    def __str__(self):
        return self.title

# models.py


class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()  
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  

    def __str__(self):
        return self.name
