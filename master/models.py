from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Shop(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class ShopHistory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    rating = models.FloatField()

class Product(models.Model):
    owner = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.TextField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(max_length=255)

class ProductHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    sold = models.IntegerField()
    rating = models.FloatField()
    stock = models.IntegerField()

class Event(models.Model):
    name = models.CharField(max_length=255)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()

class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Shop, on_delete=models.CASCADE)