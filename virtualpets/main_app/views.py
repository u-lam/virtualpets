from django.shortcuts import render, redirect
from .models import Pet, Toy
from .forms import PetForm, FeedingForm, ToyForm
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
  return render(request, 'pets/index.html', { 'pets': pets})


@login_required
def pets_detail(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  toys_pet_doesnt_have = Toy.objects.exclude(id__in = pet.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'pets/detail.html', { 
    'pet': pet, 
    'feeding_form': feeding_form,
    'toys': toys_pet_doesnt_have
  })
  
@login_required 
def assc_toy(request, pet_id, toy_id):
  Pet.objects.get(id=pet_id).toys.add(toy_id)
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
def toy_index(request):
  toys = Toy.objects.all()
  return render(request, 'toys/toy_index.html', {'toys': toys})

@login_required
def toys_detail (request, toy_id):
  toy = Toy.objects.get(id=toy_id)
  return render(request, 'toys/toy_detail.html', { 'toy': toy })


@login_required
def new_toy(request):
  if request.method == 'POST':
    form = ToyForm(request.POST)
    if form.is_valid():
      toy = form.save()
      return redirect('detail', toy.id)
  else:
    form = ToyForm()
    context = { 'form': form }
    return render(request, 'toys/toy_form.html', context) 
  

@login_required
def toys_update(request, toy_id):
  toy = Toy.objects.get(id=toy_id)
  if request.method == 'POST':
    form = ToyForm(request.POST, instance=toy)
    if form.is_valid():
      toy = form.save()
      return redirect('toys_detail', toy.id)
  else:
    form = ToyForm(instance=toy)
  return render(request, 'toys/toy_form.html', {'form': form })


@login_required
def toys_delete(request, toy_id):
  toy = Toy.objects.get(id=toy_id)
  if request.method == 'POST':
    toy.delete()
    return redirect('toys_index')
  return render(request, 'toys/toy_confirm_del.html', {'toy': toy })