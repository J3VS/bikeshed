from django.db import models

class Brand(models.Model):
     name = models.CharField(max_length=255)
     logo = models.ImageField(upload_to="images/", blank=True)

     def __str__(self):
         return  self.name

     class Meta:
         ordering = ['name']
