from django.db import models
from users.models import User


class Products(models.Model):
    STATUS_CHOICES = (
        (1, 'sale'),
        (2, 'new arrival'),
        (3, 'best seller'),
    )
    CATEGORY_CHOICES = (
        (1, 'Skirts'),
        (2, 'Panatlon'),
        (3, 'T-shirt'),
        (4, 'SweatShirt'),
        (5, 'pullover'),
    )
    category = models.SmallIntegerField(null=True, blank=True, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    image = models.ImageField(max_length=100, null=True)
    status = models.SmallIntegerField(null=True, blank=True, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class WishList(models.Model):
    customer = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    list = models.ManyToManyField(Products, null=True, blank=True)

    def __str__(self):
        return self.customer.first_name


class Voucher(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    products = models.ManyToManyField(Products, null=True, blank=True)
    date_checked = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
