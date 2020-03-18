from django import forms
from .models import Pet, Feeding

class PetForm(forms.ModelForm):
  class Meta:
    model = Pet
    fields = ['name', 'breed', 'description', 'age']

class FeedingForm(forms.ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']