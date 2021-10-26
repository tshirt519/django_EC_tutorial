from django.shortcuts import render, redirect
from django.views import View

class ProfileView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'accounts/profile.html')