from unicodedata import name
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=122)
    mobile = models.CharField(max_length=12)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=122)


class Dish(models.Model):
    dish_name = models.CharField(max_length=122)
    calories = models.IntegerField()

class Workout(models.Model):
    w_name = models.CharField(max_length=122)
    calories = models.IntegerField()

class DailyCalorieCount(models.Model):
    name = models.CharField(max_length=122)
    calorieCount = models.IntegerField()
    date = models.CharField(max_length=122)

class DailyCaloriesBurnt(models.Model):
    name = models.CharField(max_length=122)
    burntCalories = models.IntegerField()
    date = models.CharField(max_length=122)