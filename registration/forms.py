from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # Comprueba que el email no exista en la base de datos
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'telephone', 'nationality', 'photo']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'name': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Nombre'}),
            'surname': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Apellido'}),
            'telephone': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Teléfono'}),
            'nationality': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Nacionalidad'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields =['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email

