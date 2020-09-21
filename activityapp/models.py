from django.db import models
from datetime import date, time, datetime

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
class Milestone(models.Model):
    milestonename=models.CharField(max_length=255)
    project=models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    projecteddate=models.DateField(null=True, blank=True)
    finishdate=models.DateField(null=True, blank=True)
    milestonedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.milestonename

    def timeFromProjected(self):
        return (self.projecteddate - self.finishdate).days

    class Meta:
        db_table='milestone'


#activities
class Activity(models.Model):
    activityname=models.CharField(max_length=255)
    project=models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    activitydate=models.DateField(default=datetime.now)
    starttime=models.TimeField()
    endtime=models.TimeField(null=True, blank=True)
    activitydescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.activityname

    def getTimeInHours(self):
        return(self.endtime-self.startime).hours

    class Meta:
        db_table='activity'
        verbose_name_plural='activities'

#a linking table for those activities which
#contribute to one or more milestones. Doing it manually
#because not all activities will

class ActivitysMilestone(models.Model):
    activity=models.ForeignKey(Activity, on_delete=models.DO_NOTHING)
    milestone=models.ForeignKey(Milestone, on_delete=models.DO_NOTHING)

    class Meta:
        db_table="activitymilestone"



#notes
#Notes are on projects
class Note(models.Model):
    notetitle=models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    notedate=models.DateField(default=datetime.now)
    notetext=models.TextField()

    def __str__(self):
        return self.notetitle

    class Meta:
        db_table='note'