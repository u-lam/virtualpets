from django.shortcuts import render, redirect
from .models import Pet, Playground
# from django.db.models import Q
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
  return render(request, 'pets/index.html', {'pets': pets})


@login_required
def pets_detail(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  # showing all pgs for testing purposes
  playgrounds = Playground.objects.all()
  
  #  Code below currently not working. Need help!
  playgrounds_pet_not_in = Playground.objects.exclude(id__in = pet.playgrounds.all().values('id'))
 
  feeding_form = FeedingForm()
  return render(request, 'pets/detail.html', { 
    'pet': pet, 
    'feeding_form': feeding_form,
    'playgrounds': playgrounds,
    'available playgrounds': playgrounds_pet_not_in
  })
  
@login_required 
def assc_pg(request, pet_id, pg_id):
  Pet.objects.get(id=pet_id).playgrounds.add(pg_id)
  return redirect('detail', pet_id=pet_id)
  
@login_required
def leave_pg(request, pet_id, pg_id):
  Pet.objects.get(id=pet_id).playgrounds.remove(pg_id)
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
  return render(request, 'playgrounds/pg_detail.html', { 'playground': playground })


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


# @login_required
# def toys_delete(request, toy_id):
#   toy = Toy.objects.get(id=toy_id)
#   if request.method == 'POST':
#     toy.delete()
#     return redirect('toys_index')
#   return render(request, 'toys/toy_confirm_del.html', {'toy': toy })
