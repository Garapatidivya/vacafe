from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('coffee', 'Coffee'),
        ('cold', 'Cold Beverages'),
        ('snack', 'Snacks'),
        ('dessert', 'Desserts'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='coffee')

    def __str__(self):
        return self.name
