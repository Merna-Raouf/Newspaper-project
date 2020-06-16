from django.db import models

# Create your models here.
class Categoary(models.Model):
    name=models.CharField(max_length=100)


class Article(models.Model):
    Title = models.CharField(max_length=50)
    Decription = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    Article_image = models.FileField(upload_to="post_image",blank=True)
    date=models.DateField()
    writer=models.CharField(max_length=50)
    Article_Category=models.ForeignKey(Categoary,on_delete=models.CASCADE)

