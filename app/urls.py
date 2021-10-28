from django.urls import path
from app import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('product/<slug>', views.ItemDetailView.as_view(), name='product'),
]