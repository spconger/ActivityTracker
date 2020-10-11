from django.urls import path
from .views import index, addActivity

urlpatterns = [
    path('', index, name='index'),
    path('addActivity/', addActivity, name='newactivity'),
    
]