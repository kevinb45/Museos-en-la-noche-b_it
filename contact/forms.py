from django import forms

# En esta variable "c" guardamos los datos para el choice, forma simple y efectiva en este caso.
c =[("Consulta", "Consulta"), ("Consulta", "Buzón de Sugerencias")]

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu nombre'} # Toma la clase de bootstrap (toma el ancho)
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    asunt = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu asunto'}
    ), min_length=3, max_length=100)
    choices = forms.ChoiceField(choices=c, label="Tipo")    
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)