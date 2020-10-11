from django.shortcuts import render
from django.views.generic import ListView
from .models import Goal
from .forms import ActivityForm

# Create your views here.
def index(request):
    goal_list=Goal.objects.all()
    return render(request, 'activityapp/index.html', {'goal_list': goal_list})

def addActivity(request):
    form=ActivityForm

    if request.method=='POST':
        form=ActivityForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=ActivityForm()
    else:
        form=ActivityForm()
    return render(request, 'activityapp/addactivity.html', {'form': form})