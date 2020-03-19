from django.shortcuts import render, redirect
from .models import Pet, Toy
from .forms import PetForm, FeedingForm

# class-based views imports
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pets_index(request):
  pets = Pet.objects.all()
  return render(request, 'pets/index.html', { 'pets': pets})

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
  
  
def assc_toy(request, pet_id, toy_id):
  Pet.objects.get(id=pet_id).toys.add(toy_id)
  return redirect('detail', pet_id=pet_id)
  
  
def add_feeding(request, pet_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.pet_id = pet_id
    new_feeding.save()
  return redirect('detail', pet_id=pet_id)


def new_pet(request):
  if request.method == 'POST':
    form = PetForm(request.POST)
    if form.is_valid():
      pet = form.save()
      return redirect('detail', pet.id)
  else:
    form = PetForm()
    context = { 'form': form }
    return render(request, 'pets/pet_form.html', context)


# ----------- TOYS -----------

# Goes to toy_index.html
class ToyIndex(ListView):
  model = Toy

# Goes to toy_detail.html
class ToyDetail(DetailView):
  model = Toy
  
class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'
  
class ToyUpdate(UpdateView):
  model = Toy
  fields = '__all__'
  
class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'