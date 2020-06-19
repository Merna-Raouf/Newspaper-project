from django.contrib.auth import get_user_model
from django.db import models

class Categoary(models.Model):
    name=models.CharField(max_length=100)

class Article(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='Article',
    null = True
    )
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    Article_image = models.FileField(upload_to="post_image", blank=True)
    date = models.DateField()
    Article_Category = models.ForeignKey(Categoary, on_delete=models.CASCADE)


