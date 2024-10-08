from django.shortcuts import render, redirect
from Petstagram.pets.models import Pet
from Petstagram.pets.forms import PetBaseForm


# Create your views here.
def add_pet_page(request):
    form = PetBaseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile-details', pk=1)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context)


def delete_pet_page(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')


def pet_page_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet_page(request ,username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')
