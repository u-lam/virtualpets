from django.shortcuts import render, redirect
from .models import Pet, Playground
from django.db.models import Q, F, Exists
from django.core.exceptions import ValidationError
from .forms import PetForm, FeedingForm, PlaygroundForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# class-based views imports
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def avail_pets(request):
  pets = Pet.objects.filter(user=None)
  return render(request, 'avail_pets.html', { 'pets': pets })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - please try again'
  
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)

@login_required
def pets_index(request):
  pets = Pet.objects.filter(user=request.user)
  wild_pets = Pet.objects.exclude(user=request.user)
  return render(request, 'pets/index.html', {'pets': pets, 'wild_pets': wild_pets})


@login_required
def pets_detail(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  playgrounds_pet_not_in = Playground.objects.exclude(id__in = pet.playgrounds.all().values_list('id'))
  feeding_form = FeedingForm()
  # TESTING
  # playground = Playground.objects.all()
  # print('he', pet)
  # print('hel', playground)
  # print('hello', pet.playgrounds)
  # print('hello', playground.pets)
  
  return render(request, 'pets/detail.html', { 
    'pet': pet, 
    'feeding_form': feeding_form,
    'playgrounds': playgrounds_pet_not_in
  })

@login_required 
def assc_pg(request, pet_id, pg_id):
  pet = Pet.objects.get(id=pet_id)
  playground = Playground.objects.get(id=pg_id) 
  # Add pg to pet
  pet.playgrounds.add(pg_id)
  # Increment pet count
  if playground.current_capacity < playground.max_capacity:
    Playground.objects.filter(id=pg_id).update(current_capacity=F('current_capacity') + 1)
  
  # HELP: if pet is already in a pg (pet.playgrounds.count == 1), do not add more pg. 
  return redirect('detail', pet_id=pet_id)   
  
  
  
@login_required
def leave_pg(request, pet_id, pg_id):
  Pet.objects.get(id=pet_id).playgrounds.remove(pg_id)
  playground = Playground.objects.get(id=pg_id) 
  if playground.current_capacity > 0:
    Playground.objects.filter(id=pg_id).update(current_capacity=F('current_capacity') - 1)
  return redirect('detail', pet_id=pet_id)  
  
@login_required 
def add_feeding(request, pet_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.pet_id = pet_id
    new_feeding.save()
  return redirect('detail', pet_id=pet_id)

@login_required
def new_pet(request):
  if request.method == 'POST':
    form = PetForm(request.POST)
    if form.is_valid():
      pet = form.save(commit=False)
      pet.user = request.user
      pet.save()
      return redirect('detail', pet.id)
  else:
    form = PetForm()
    context = { 'form': form }
    return render(request, 'pets/pet_form.html', context)


@login_required
def pets_update(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  
  if request.method == 'POST':
    form = PetForm(request.POST, instance=pet)
    if form.is_valid():
      pet = form.save()
      return redirect('detail', pet.id)
  else:
    form = PetForm(instance=pet)
  return render(request, 'pets/pet_form.html', { 'form': form })


@login_required
def pets_delete(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  if request.method == 'POST':
    pet.delete()
    return redirect('index')
  else:  #Get method
    context = { 'pet': pet } 
    return render(request, 'pets/pet_confirm_del.html', context)
  
  
# ----------- TOYS -----------

@login_required
def pg_index(request):
  playgrounds = Playground.objects.all()
  return render(request, 'playgrounds/pg_index.html', {'playgrounds': playgrounds })

@login_required
def pg_detail (request, pg_id):
  playground = Playground.objects.get(id=pg_id)
  pets = Pet.objects.filter(user=request.user)
  
  # HELP:  How to filter this so only pets that are in this playground shows up. Right now, all user's pets shows up
  return render(request, 'playgrounds/pg_detail.html', {
    'playground': playground,
    'pets': pets
  })



# @login_required
# def new_toy(request):
#   if request.method == 'POST':
#     form = ToyForm(request.POST)
#     if form.is_valid():
#       toy = form.save()
#       return redirect('detail', toy.id)
#   else:
#     form = ToyForm()
#     context = { 'form': form }
#     return render(request, 'toys/toy_form.html', context) 
  

@login_required
def pg_update(request, pg_id):
  playground = Playground.objects.get(id=pg_id)
  if request.method == 'POST':
    form = PlaygroundForm(request.POST, instance=playground)
    if form.is_valid():
      playground = form.save()
      return redirect('pg_detail', playground.id)
  else:
    form = PlaygroundForm(instance=playground)
  return render(request, 'playgrounds/pg_form.html', {'form': form })
