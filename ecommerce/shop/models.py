from django.db import models

# Create your models here.
class Categorie_produit(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added'] 