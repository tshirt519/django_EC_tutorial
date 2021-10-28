from django.db import models
from django.utils import timezone

class Item(models.Model):
  title = models.CharField(max_length=100)
  price = models.IntegerField()
  categroy = models.CharField(max_length=100)
  slug = models.SlugField()
  description = models.TextField()
  image = models.ImageField(upload_to='images')
  created = models.DateField('作成日', default=timezone.now)

  def __str__(self):
    return self.title