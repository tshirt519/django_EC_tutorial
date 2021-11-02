from django.db import models
from django.utils import timezone
from django.conf import settings

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

class OrderItem(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ordered = models.BooleanField(default=False)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)

  def get_total_item_price(self):
    return self.quantity * self.item.price

  def __str__(self):
    return f"{self.item.title}:{self.quantity}"

class Order(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  items = models.ManyToManyField(OrderItem)
  start_date = models.DateTimeField(auto_now_add=True)
  ordered_date = models.DateTimeField()
  ordered = models.BooleanField(default=False)

  def get_total(self):
    total = 0
    for order_item in self.item.all():
      total += order_item.get_total_price()
    return total

  def __str__(self):
    return self.user.email