from django.db import models
from django.contrib.auth.models import User

from user.models import Rentee


class Type(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Rent(models.Model):
    rentee = models.ForeignKey(Rentee, null=True, on_delete=models.SET_NULL)
    renter = models.ForeignKey(User, null=True, related_name='renter', on_delete=models.SET_NULL)
    entered_by = models.ForeignKey(User, null=True, related_name='entered_person', on_delete=models.SET_NULL)
    total_cost = models.PositiveIntegerField()
    paid = models.PositiveIntegerField()
    rented_date = models.DateTimeField(auto_now_add=True)
    closed_date = models.DateField()
    #
    # def __str__(self):
    #     return self.rentee.name


class RentedItem(models.Model):
    record = models.ForeignKey(Rent, null=True, related_name='rented_item', on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.item.name
