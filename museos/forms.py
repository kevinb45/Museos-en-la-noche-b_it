from django import forms
from .models import Museo,Actividades
from django.contrib.auth.models import User

class MuseoForm(forms.ModelForm):


    colection = forms.ChoiceField(label='Coleccion',choices=Museo.COLECCIONES,widget=forms.Select(attrs={'class':'form-control'}))
    district = forms.ChoiceField(label='Barrio',choices=Museo.BARRIOS,widget=forms.Select(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control'}),required=False)
    opening_hour = forms.ChoiceField(label='Apertura',choices=Museo.TIME_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    close_hour = forms.ChoiceField(label='Cierra',choices=Museo.TIME_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    accesibilty = forms.BooleanField(required=False,initial=False,label='Accesibilidad para discapacitados')
    wifi = forms.BooleanField(required=False,initial=False,label='Wi-Fi')
    coffee = forms.BooleanField(required=False,initial=False,label='Cafeteria')
    active = forms.BooleanField(required=False,initial=True,label='Activo?')
    #activities = forms.ModelMultipleChoiceField(label='Actividades',queryset=Actividades.objects.filter(author_id=1),widget=forms.Select(attrs={'class':'form-control','multiple':'true'}))

    readonly_fields = ('author',)

    def get_readonly_fields(self,request, obj=None):
        if request.user.is_superuser or request.user.groups.filter(name="Admin").exists():
            return ()
        else: 
            return ('author',)

    class Meta:
        model = Museo
        
        fields = ['title', 'content','colection','address','district','web','email','telephone','opening_hour','close_hour','accesibilty','wifi','coffee','photo1','photo2','photo3','activities']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'web': forms.TextInput(attrs={'class':'form-control'}),
            'telephone': forms.TextInput(attrs={'class':'form-control'}),
            'photo1': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'photo2': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'photo3': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
        }
        labels = {
            'title': '', 'content':''
        }
    



class ActividadesForm(forms.ModelForm):

    opening_hour = forms.ChoiceField(label='Apertura',choices=Museo.TIME_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    close_hour = forms.ChoiceField(label='Cierra',choices=Museo.TIME_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    accesibilty = forms.BooleanField(required=False,initial=False,label='Accesibilidad para discapacitados')
    active = forms.BooleanField(required=False,initial=True,label='Activo?')

    class Meta:
        model = Actividades
        fields = ['title', 'content','opening_hour','close_hour','accesibilty','active']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class':'form-control'})
        }
        labels = {
            'title': '', 'content':''
        }



