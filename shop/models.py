from django.db import models
from django.utils import timezone


# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Address(models.Model):
    street = models.CharField(max_length=400)
    ward = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Customer(models.Model):
    fullname = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL).null = True
    email = models.EmailField()
    phone = models.CharField(max_length=11)


class Product(models.Model):
    name = models.CharField(max_length=400)
    type = models.CharField(max_length=400)
    amount_remain = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=400)
    quantity = models.IntegerField()
    price_sale = models.FloatField()
    shop_name = models.CharField(max_length=400)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Comment(models.Model):
    title = models.CharField(max_length=400)
    content = models.CharField(max_length=400)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Order(models.Model):
    date_create = timezone.now()
    status = models.CharField(max_length=400)


class Shipment(models.Model):
    destination = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=400)
    cost = models.FloatField(default=15000)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Payment(models.Model):
    type = models.CharField(max_length=400)
    total = models.FloatField()
