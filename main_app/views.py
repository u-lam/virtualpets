from django.shortcuts import render, redirect
from .models import Pet, Toy
from .forms import PetForm, FeedingForm, ToyForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# class-based views imports
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


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
  # Get the ID of one pet 
  pet = Pet.objects.get(id=pet_id)
  
  toys_pet_doesnt_have = Toy.objects.exclude(id__in = pet.toys.all().values_list('id'))
  
  # create a new feeding form to be rendered below with the template
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


# ----------- TOYS -----------

# Goes to toy_index.html
@login_required
def toy_index(request):
  toys = Toy.objects.all()
  return render(request, 'toys/toy_index.html', {'toys': toys})

# Goes to toy_detail.html
class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy
  
# class ToyCreate(CreateView):
#   model = Toy
#   fields = '__all__'

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
  
class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = '__all__'
  
class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'