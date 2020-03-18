from django.db import models
from django.urls import reverse
from datetime import date


MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=50)
  material = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name
  
  # this method is required for CBV usage
  def get_absolute_url(self):
      return reverse("toys_detail", kwargs={"pk": self.id})
  
  
class Pet(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=200)
  age = models.IntegerField()
  color = models.CharField(max_length=20)
  
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