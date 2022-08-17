from django.db import models

# Create your models here.
class Categorie_produit(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

class Produit(models.Model):
    designation = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    categorie = models.ForeignKey(Categorie_produit, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
