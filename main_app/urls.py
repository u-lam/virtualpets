from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pets/', views.pets_index, name='index'),
  path('pets/new', views.new_pet, name='new_pet'),
  path('pets/<int:pet_id>', views.pets_detail, name='detail'),
  path('pets/<int:pet_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  
  path('toys/', views.ToyIndex.as_view(), name='toys_index'),
  path('toys/<int:pk>', views.ToyDetail.as_views(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_views(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_views(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_views(), name='toys_delete')
]