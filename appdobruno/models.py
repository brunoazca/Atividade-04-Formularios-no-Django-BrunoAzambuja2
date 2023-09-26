from django.db import models
from django.utils.text import slugify

class Sports(models.Model):
  title=models.CharField(max_length=50)
  num_of_players=models.CharField(max_length=50)
  creation_date=models.DateField(max_length=50)
  like_rank=models.IntegerField()
  slug = models.SlugField(unique=True)
  
  def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Sports, self).save(*args, **kwargs)
    
  def __str__(self):
      return self.title
    
class Routine(models.Model):
  FREQUENCY=[
    ("N","Never"),
    ("S","Sometimes"),
    ("A","Always"),
  ]
  title=models.CharField(max_length=50)
  place=models.CharField(max_length=50)
  frequency=models.CharField(max_length=1,choices=FREQUENCY)
  like_rank=models.IntegerField()

    
class Activities(models.Model):
  FREQUENCY=[
    ("N","Never"),
    ("S","Sometimes"),
    ("A","Always"),
  ]
  EFFORT=[
    ("L","Little"),
    ("M","Medium"),
    ("B","Big"),
  ]
  title=models.CharField(max_length=50)
  effort=models.CharField(max_length=1,choices=EFFORT)
  frequency=models.CharField(max_length=1,choices=FREQUENCY)
  like_rank=models.IntegerField()
  slug = models.SlugField(unique=True)
  
  def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Activities, self).save(*args, **kwargs)
    
  def __str__(self):
      return self.title
