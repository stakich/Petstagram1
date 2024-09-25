from django.shortcuts import render


# Create your views here.
def add_photo_page(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details_page(request, pk):
    return render(request, 'photos/photo-details-page.html')


def photo_edit_page(request, pk):
    return render(request, 'photos/photo-edit-page.html')