from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
