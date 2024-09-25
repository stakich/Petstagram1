from django.urls import path, include
from Petstagram.accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.details_page, name='profile-details'),
        path('edit/', views.edit_page, name='profile-edit'),
        path('delete/', views.profile_delete, name='profile-delete'),
    ])),
]