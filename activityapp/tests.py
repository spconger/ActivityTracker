from django.test import TestCase
from datetime import date
from .models import Goal, Category, Project

class ProjectTest(TestCase):
    def setUp(self):
        g=Goal(goaltext='Some Goal')
        c=Category(categoryname='testing')
        start=date(2020,9,18)
        end=date(2020,9,22)
        self.p = Project(projectname='project',goal=g,category=c, projectstartdate=start, projectenddate=end, projectdescription='some project')
    
    def test_date_function(self):
        self.assertTrue(p.timeInDays(), 4)

           
