from django.db import models
from users.models import User


class Products(models.Model):
    STATUS_CHOICES = (
        (1, 'sale'),
        (2, 'new arrival'),
        (3, 'best seller'),
    )
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    image = models.ImageField(max_length=100, null=True)
    status = models.SmallIntegerField(null=True, blank=True, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class WishList(models.Model):
    customer = models.OneToOneField(User, null=True, blank=True , on_delete=models.CASCADE)
    list = models.ManyToManyField(Products, null=True, blank=True)

    def __str__(self):
        return self.customer.first_name
