from django.shortcuts import render, redirect
from Petstagram.photos.models import Photo
from Petstagram.photos import forms


# Create your views here.

def add_photo_page(request):
    form = forms.PhotoAddForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'photos/photo-add-page.html', context)


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
