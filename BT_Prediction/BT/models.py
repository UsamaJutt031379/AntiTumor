from django.db import models

class published_articles(models.Model):
       
       name = models.CharField(max_length=50)
       definantion = models.TextField(max_length=500)
       overview = models.TextField(max_length=5000)
       symptoms = models.TextField(max_length=5000)
       diagnosis = models.TextField(max_length=5000)
       treatment = models.TextField(max_length=5000)
       recovery = models.TextField(max_length=5000)

       def __str__(self):
          return self.name

