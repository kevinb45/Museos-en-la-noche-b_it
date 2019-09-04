from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            asunt = request.POST.get('asunt', '')
            choices = request.POST.get('choices', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "Museos en la noche({}): Nuevo Mensaje de contacto".format(choices),
                "De {} <{}>\n\nEscribió:\n\n{}\n\n{}".format(name, email, asunt, content),
                "no-contestar@inbox.mailtrap.io",
                ["nicodeaz72@gmail.com"],
                reply_to=[email]
            )
            # Con el try confirmamos que funcione.
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK     
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ibo bien, redireccionamos a FAIL      
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})
