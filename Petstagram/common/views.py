from django.shortcuts import render, redirect, resolve_url
from Petstagram.photos.models import Photo
from Petstagram.common.models import Like
from pyperclip import copy

# Create your views here.

def home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, pk):
    photo = Photo.objects.get(pk=pk)

    liked_object = Like.objects.filter(to_photo_id=pk).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{pk}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')