from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Snack(models.Model):
    name=models.CharField(max_length=64,help_text="name of the snack")
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    desc=models.TextField(default="no desc available")


    def __str__(self):
        return self.name

