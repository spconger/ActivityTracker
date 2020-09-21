from django.db import models
from datetime import date

# Create your models here.

#Goals
class Goal(models.Model):
    goaltext=models.CharField(max_length=255)

    def __str__(self):
        return self.goaltext

    class Meta:
        db_table='goal'

#categories
class Category(models.Model):
    categoryname=models.CharField(max_length=255)

    def __str__(self):
        return self.categoryname

    class Meta:
        db_table='category'
        verbose_name_plural='categories'

#projects

class Project(models.Model):
    projectname=models.CharField(max_length=255)
    goal=models.ForeignKey(Goal, on_delete=models.DO_NOTHING)
    category=models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    projectstartdate=models.DateField()
    projectenddate=models.DateField(null=True, blank=True)
    projectdescription=models.TextField()

    def __str__(self):
        return self.projectname

    def timInDays(self):
        return (self.projectenddate-self.projectstartdate).days

    class Meta:
        db_table='project'

#milestones


#activities

#notes