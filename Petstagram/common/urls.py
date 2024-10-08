from django.urls import path, include
from Petstagram.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('like/<int:pk>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>/', views.copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>/', views.comment_functionality, name='comment'),
]