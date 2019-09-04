from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args,  **kwargs):
        return render(request, self.template_name, {'title':"Museos en la noche"})  

class FaqPageView(TemplateView):
    template_name = "core/faq.html"

class Fu5ionPageView(TemplateView):
    template_name = "core/fu5ion.html"    

class RecorridosPageView(TemplateView):
    template_name = "core/recorridos.html"
