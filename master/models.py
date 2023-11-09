from django.db import models

class Category(models.Model):
    name = models.CharField()

class Shop(models.Model):
    name = models.CharField()
    location = models.CharField()

class ShopHistory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    rating = models.DecimalField()

class Product(models.Model):
    owner = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.TextField()
    name = models.CharField()
    description = models.TextField()
    condition = models.CharField()

class ProductHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField()
    sold = models.IntegerField()
    rating = models.DecimalField()
    stock = models.IntegerField()

class Event(models.Model):
    name = models.CharField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()

class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Shop, on_delete=models.CASCADE)