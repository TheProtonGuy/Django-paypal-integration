from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
