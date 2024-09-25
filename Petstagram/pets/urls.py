from django.urls import path, include
from Petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet_page, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_page_details, name='pet-details'),
        path('edit/', views.edit_pet_page, name='edit-pet'),
        path('delete/', views.delete_pet_page, name='delete-pet'),
    ]))
]