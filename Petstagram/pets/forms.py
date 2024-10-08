from django import forms
from Petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet Name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link to image'})
        }

        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image'
        }


class PetEditForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True
            self.fields[field].readonly = True