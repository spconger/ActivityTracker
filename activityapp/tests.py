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
    
    def test_dateFunction(self):
        self.assertEqual(self.p.timeInDays(), 4)

    def test_string(self):
        self.assertEqual(str(self.p), 'project')

           
