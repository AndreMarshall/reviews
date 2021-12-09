from django.db import models

# Create your models here.


class Movies(models.Model):
    name = models.CharField(max_length=200)
    review = models.CharField(max_length=5000)
    rating = models.IntegerField()
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
