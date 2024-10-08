from django.urls import path, include
from Petstagram.photos import views


urlpatterns = [
    path('add/', views.add_photo_page, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.show_photo_details, name='photo-details'),
        path('edit/', views.photo_edit_page, name='edit-photo')
    ])),
]