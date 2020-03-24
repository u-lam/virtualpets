from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('avail/', views.avail_pets, name='avail_pets'),
  path('avail/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
  
  path('pets/', views.pets_index, name='index'),
  path('pets/new/', views.new_pet, name='new_pet'),
  path('pets/<int:pet_id>/', views.pets_detail, name='detail'),
  path('pets/<int:pet_id>/edit/', views.pets_update, name='pets_update'),
  path('pets/<int:pet_id>/delete/', views.pets_delete, name='pets_delete'),
  path('pets/<int:pet_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('pets/<int:pet_id>/assc_pg/<int:pg_id>', views.assc_pg, name='assc_pg'),
  path('pets/<int:pet_id>/leave_pg/<int:pg_id>', views.leave_pg, name='leave_pg'),
  
  path('pg/', views.pg_index, name='pg_index'),
  path('pg/<int:pg_id>/', views.pg_detail, name='pg_detail'),
    path('pg/<int:pg_id>/update/', views.pg_update, name='pg_update'),

  path('user/profile/', views.user_profile, name='user_profile'),
  path('user/update/', views.user_update, name='user_update'),

  path('accounts/signup/', views.signup, name='signup'),
]
