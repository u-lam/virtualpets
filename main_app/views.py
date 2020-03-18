from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm, FeedingForm

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pets_index(request):
  pets = Pet.objects.all()
  return render(request, 'pets/index.html', { 'pets': pets})

def pets_detail(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  feeding_form = FeedingForm()
  return render(request, 'pets/detail.html', { 
    'pet': pet, 'feeding_form': feeding_form
  })
  
def add_feeding(request, pet_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.pet_id = pet_id
    new_feeding.save()
  return redirect('detail', pet_id=pet_id)
