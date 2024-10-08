from django.shortcuts import render, redirect
from Petstagram.pets.models import Pet
from Petstagram.pets import forms


# Create your views here.
def add_pet_page(request):
    form = forms.PetBaseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile-details', pk=1)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context)


def delete_pet_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    form = forms.PetDeleteForm(instance=pet)
    context = {
        'form': form
    }

    return render(request, 'pets/pet-delete-page.html', context)


def pet_page_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet_page(request,username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'POST':
        form = forms.PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    else:
        form = forms.PetEditForm(instance=pet)

    context = {
        'form': form
    }
    return render(request, 'pets/pet-edit-page.html', context)

