from django.shortcuts import render
from Petstagram.photos.models import Photo


# Create your views here.

def add_photo_page(request):
    return render(request, 'photos/photo-add-page.html')


def show_photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo_likes = photo.like_set.all()
    comments = photo.comments.all()

    context = {
        'photo': photo,
        'photo_likes': photo_likes,
        'comments': comments,  # Change this to 'comments' instead of 'photo_comments'
    }

    return render(request, 'photos/photo-details-page.html', context)


def photo_edit_page(request, pk):
    return render(request, 'photos/photo-edit-page.html')
