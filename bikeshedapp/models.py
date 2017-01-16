from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

BIKECHOICE = (
    ('', 'Select Type'),
    ('M', 'Mountain'),
    ('R', 'Road'),
    ('H', 'Hybrid'),
)

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Brand(models.Model):
     name = models.CharField(max_length=255)
     logo = models.ImageField(upload_to="images/", blank=True)

     def __str__(self):
         return  self.name

     class Meta:
         ordering = ['name']

class Bike(models.Model):
    brand = models.ForeignKey(Brand)
    type = models.CharField(max_length=1, choices=BIKECHOICE)
    created_by = models.ForeignKey(User)
    created_date = models.DateTimeField();
    model = models.CharField(max_length=255)
    headline = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="uploads/", blank=True, default='None/no-img.png')
    size = IntegerRangeField(min_value=12, max_value=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return  self.model

    class Meta:
        ordering = ['price']
