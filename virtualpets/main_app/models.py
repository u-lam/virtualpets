from django.db import models
from django.urls import reverse
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# Setting capacity playground at 5 max for easy testing
class Playground(models.Model):
  name = models.CharField(max_length=20)
  virtual_location = models.CharField(max_length=50)
  current_capacity = models.IntegerField(
    validators= [MaxValueValidator(5), MinValueValidator(0)])
  max_capacity = models.IntegerField(
    validators= [MaxValueValidator(5), MinValueValidator(0)])
  features = models.TextField(max_length=200)
  
  def __str__(self):
    return self.name
  
  # this method is required for CBV usage   -- OLD CODE. Keeping here for now in case we need it later.
  # def get_absolute_url(self):
  #     return reverse("toys_detail", kwargs={"pk": self.id})
  
  
class Pet(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=200)
  age = models.IntegerField()
  color = models.CharField(max_length=20)
  
  playground = models.ForeignKey(Playground, on_delete=models.CASCADE, null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
  
class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    'Meal of the day',
    max_length=1,
    choices=MEALS,
    # defaults to Breakfast meal
    default=MEALS[0][0]
  )
  
  pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.get_meal_display()} on {self.date} for {self.pet}'
  
  class Meta:
    ordering = ['-date']