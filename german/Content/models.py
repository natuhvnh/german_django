from django.db import models

# Create your models here.
class Card(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField()
  image = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.title

class Intro(models.Model):
  heading = models.CharField(max_length=100)
  intro = models.TextField()
  icon = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.heading

class Service(models.Model):
  service = models.CharField(max_length=100)
  detail = models.TextField()
  image = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.service

class Slider(models.Model):
  original = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)