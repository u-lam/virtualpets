from django import forms
from .models import Pet, Feeding, Playground

class PlaygroundForm(forms.ModelForm):
  class Meta:
    model = Playground
    fields = ['name', 'virtual_location', 'current_capacity', 'max_capacity', 'features']

class PetForm(forms.ModelForm):
  class Meta:
    model = Pet
    fields = ['name', 'breed', 'description', 'age']
   
class FeedingForm(forms.ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']