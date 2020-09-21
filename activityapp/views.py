from django.shortcuts import render
from django.views.generic import ListView
from .models import Goal

# Create your views here.
def index(request):
    goal_list=Goal.objects.all()
    return render(request, 'activityapp/index.html', {'goal_list': goal_list})