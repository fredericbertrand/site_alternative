from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
Nutrifood
class Produits(models.Model):
    code = models.BigIntegerField()
    product_name = models.CharField(max_length=50)
    categories = models.CharField(max_length=150)
    ingredients = models.CharField(max_length=200)
    nutriscore_score = models.IntegerField()
