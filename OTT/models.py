from django.db import models
import os
# Create your models here.
class movie(models.Model):
  title = models.CharField(null=True,max_length=20)
  grade = models.CharField(null=True,max_length=10)
  nation = models.CharField(null=True,max_length=10)
  distribution = models.CharField(null=True,max_length=10)
  running_time = models.IntegerField(null=True,) 
  information = models.TextField(null=True,)
  ralease_date = models.DateField(null=True,)
  genre = models.TextField(null=True,)
  actor = models.CharField(null=True,max_length=100)
  director = models.CharField(null=True,max_length=100)

  def __str__(self):
    return self.title  
  
  def get_absolute_url(self):
    return f'/Main/{self.pk}'
