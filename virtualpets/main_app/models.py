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

class Playground(models.Model):
  name = models.CharField(max_length=20)
  virtual_location = models.CharField(max_length=50)
  current_capacity = models.IntegerField(
    default = 0,
    # changed max value to 3 for ease of testing
    validators= [MaxValueValidator(3), MinValueValidator(0)])
  max_capacity = models.IntegerField(
    default = 0,
    validators= [MaxValueValidator(3), MinValueValidator(0)])
  features = models.TextField(max_length=200)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("pg_detail", kwargs={"pk": self.id})
  

    

class Pet(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=200)
  age = models.IntegerField(blank=False)  #required field
  color = models.CharField(max_length=20)
  
  # null=True is db-related; will store the value as 'null' in DB fk, 
  # blank=True is validation-related; here it will not require an association, so a pet does NOT have to belong to a user or playground
  # related_name lets us defining a meaningful name for the reverse relationship
  playgrounds = models.ManyToManyField(Playground, blank=True, related_name='pets')
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='pets')
  
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