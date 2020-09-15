from django.db import models

class Produit(models.Model):
    ingrédient = models.CharField(max_length=200)
