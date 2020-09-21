from django.contrib import admin
from .models import Goal, Project, Activity, Milestone, Category, Note, ActivitysMilestone

# Register your models here.
admin.site.register(Goal)
admin.site.register(Project)
admin.site.register(Activity)
admin.site.register(Milestone)
admin.site.register(Category)
admin.site.register(Note)
admin.site.register(ActivitysMilestone)
