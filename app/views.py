from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Item

class IndexView(TemplateView):
  def get(self, request, *args, **kwargs):
    item_data = Item.objects.all()
    return render(request, 'app/index.html', {
      'item_data': item_data
    })
