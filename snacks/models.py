from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Snack(models.Model):
    name=models.CharField(max_length=64,help_text="name of the snack")
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    rank=models.IntegerField()
    desc=models.TextField(default="no des available")


    def __str__(self):
        return self.name

