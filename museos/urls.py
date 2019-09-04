from django.urls import path
from django.conf.urls import url
from .views import MuseoListView, MuseoDetailView, MuseoCreate, MuseoUpdate, MuseoDelete, ActividadesTemplateView, MyMuseoView, MyActivitiesView, MuseoCreateAct, MuseoUpdateAct, MuseoDeleteAct

museos_patterns = ([
    path('', MuseoListView.as_view(), name='museos'),
    path('act/', MyActivitiesView.as_view(), name='act'),
    path('my/', MyMuseoView.as_view(), name='my'),
    path('<int:pk>/<slug:slug>/', MuseoDetailView.as_view(), name='museo'),
    path('create/', MuseoCreate.as_view(), name='create'),
    path('update/<int:pk>', MuseoUpdate.as_view(), name='update'),
    path('delete/<int:pk>', MuseoDelete.as_view(), name='delete'),
    path('actividades/<int:actividades_id>', ActividadesTemplateView.as_view(), name='actividades'),
    path('createact/', MuseoCreateAct.as_view(), name='createact'),
    path('updateact/<int:pk>', MuseoUpdateAct.as_view(), name='updateact'),
    path('deleteact/<int:pk>', MuseoDeleteAct.as_view(), name='deleteact'),



],'museos')

