from django.shortcuts import render, redirect
from Petstagram.photos.models import Photo
from Petstagram.common.models import Like


# Create your views here.

def home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)

    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')