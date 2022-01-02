from django.db import models

# Create your models here.


class CardInfo(models.Model):
    card_number = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)