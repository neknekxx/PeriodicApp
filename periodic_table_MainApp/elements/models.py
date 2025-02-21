from django.db import models

class Element(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5, unique=True)
    atomic_number = models.IntegerField(unique=True)
    atomic_weight = models.FloatField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='element_images/', blank=True, null=True)  # ✅ Added image field

    def __str__(self):
        return f"{self.name} ({self.symbol})"
