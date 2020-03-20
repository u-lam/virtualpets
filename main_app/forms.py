from django import forms
from .models import Pet, Feeding, Toy

class ToyForm(forms.ModelForm):
  class Meta:
    model = Toy
    fields = ['name', 'color', 'material']

class PetForm(forms.ModelForm):
  class Meta:
    model = Pet
    fields = ['name', 'breed', 'description', 'age']

class FeedingForm(forms.ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']