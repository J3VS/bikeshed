from django.db import models
from django.contrib.auth.models import User
from integer_range_field import IntegerRangeField
from brand import Brand

BIKECHOICE = (
    ('', 'Select Type'),
    ('M', 'Mountain'),
    ('R', 'Road'),
    ('H', 'Hybrid'),
)

class Bike(models.Model):
    brand = models.ForeignKey(Brand)
    type = models.CharField(max_length=1, choices=BIKECHOICE)
    created_by = models.ForeignKey(User)
    created_date = models.DateTimeField();
    model = models.CharField(max_length=255)
    headline = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="uploads/")
    size = IntegerRangeField(min_value=12, max_value=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return  self.model

    class Meta:
        ordering = ['-price']
