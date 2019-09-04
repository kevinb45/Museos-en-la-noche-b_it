from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SuperuserRequiredMixin, AjaxResponseMixin, JSONResponseMixin
from django.shortcuts import redirect
from .models import Museo, Actividades
from .forms import MuseoForm,ActividadesForm


class MuseoListView(ListView):
    model = Museo
    template_name = "templates/museo_list.html"
    paginate_by = 10

    def get_queryset(self):
        address_val = self.request.GET.get('address', '')
        district_val = self.request.GET.get('district', '')
        colection_val = self.request.GET.get('colection', '')
        accesibilty_val = self.request.GET.get('accesibilty', '')
        wifi_val = self.request.GET.get('wifi', '')
        coffee_val = self.request.GET.get('coffee', '')
        order = self.request.GET.get('orderby', 'title')
        active = True


        new_context = Museo.objects.filter(
            address__icontains=address_val,
        ).filter(
            district__icontains=district_val,
        ).filter(
            colection__icontains=colection_val,
        ).filter(
            wifi__icontains=wifi_val,
        ).filter(
            coffee__icontains=coffee_val,
        ).filter(
            accesibilty__icontains=accesibilty_val,
        ).filter(
            active=active,
        ).order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(MuseoListView, self).get_context_data(**kwargs)
        context['address'] = self.request.GET.get('address', '')
        context['district'] = self.request.GET.get('district', '')
        context['colection'] = self.request.GET.get('colection', '')
        context['wifi'] = self.request.GET.get('wifi', '')
        context['coffee'] = self.request.GET.get('coffee', '')
        context['accesibilty'] = self.request.GET.get('accesibilty', '')
        context['orderby'] = self.request.GET.get('orderby', 'title')
        context['active'] = True

        return context

        


class ActividadesTemplateView(TemplateView):
    model = Actividades
    template_name="museos/museo_detail.html"
     
    def get_context_data(self, *args, **kwargs):
       actividades = Actividades.objects.all()
       return {'actividades': actividades}

class MuseoDetailView(DetailView):
    model = Museo
    second_model= Actividades

    #def queryset(self):
     #   actividades =  Actividades.objects.all()
      #  return {'actividades': actividades}
    def get_context_data(self, **kwargs):
        context = super(MuseoDetailView, self).get_context_data(**kwargs)
        context['act'] = Actividades.objects.all()
        return context

class MyMuseoView(ListView):
    model = Museo
    template_name="museos/my_museo_list.html"
    def get_queryset(self):
        author_id = self.request.user

        context = Museo.objects.filter(
            author_id= author_id,
        )
        return context

    def get_context_data(self, **kwargs):
        context = super(MyMuseoView, self).get_context_data(**kwargs)
        context['author_id'] = self.request.user
        return context

class MyActivitiesView(ListView):
    model = Actividades
    template_name="actividades/actividades_list.html"

    def get_queryset(self):
        author_id = self.request.user

        context = Actividades.objects.filter(
            author_id= author_id,
        )
        return context

class ViewActividades(DetailView):
    model = Actividades
    template_name="museos/museo_detail.html"

@method_decorator(staff_member_required, name='dispatch')
class MuseoCreate(CreateView):
    model = Museo
    form_class = MuseoForm
    success_url = reverse_lazy('museos:museos')
    
    def form_valid(self, form_class):
        form_class.instance.author = self.request.user
        return super(MuseoCreate, self).form_valid(form_class)
    
    
@method_decorator(staff_member_required, name='dispatch')
class MuseoUpdate(UpdateView):
    model = Museo
    form_class = MuseoForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('museos:update', args=[self.object.id]) + '?ok'
    
    def form_valid(self, form_class):
        form_class.instance.author = self.request.user
        return super(MuseoUpdate, self).form_valid(form_class)

@method_decorator(staff_member_required, name='dispatch')
class MuseoDelete(DeleteView):
    model = Museo
    success_url = reverse_lazy('museos:museos')

@method_decorator(staff_member_required, name='dispatch')
class MuseoCreateAct(CreateView):
    model = Actividades
    template_name="actividades/actividades_form.html"

    form_class = ActividadesForm
    success_url = reverse_lazy('museos:act')

    def form_valid(self, form_class):
        form_class.instance.author = self.request.user
        return super(MuseoCreateAct, self).form_valid(form_class)

    



    
@method_decorator(staff_member_required, name='dispatch')
class MuseoUpdateAct(UpdateView):
    model = Actividades
    form_class = ActividadesForm
    template_name="actividades/actividades_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('museos:updateact', args=[self.object.id]) + '?ok'

    def form_valid(self, form_class):
        form_class.instance.author = self.request.user
        return super(MuseoUpdateAct, self).form_valid(form_class)

@method_decorator(staff_member_required, name='dispatch')
class MuseoDeleteAct(DeleteView):
    model = Actividades
    template_name="actividades/actividades_confirm_delete.html"
    success_url = reverse_lazy('museos:act')
