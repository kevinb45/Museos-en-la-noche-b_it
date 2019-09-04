from django.urls import path
from .views import HomePageView, FaqPageView, RecorridosPageView, Fu5ionPageView

urlpatterns = [
    # Path de Home
    path('', HomePageView.as_view(), name="home"),
    # Path de Faq
    path('faq/', FaqPageView.as_view(), name="faq"),
    # Path de Fu5ion
    path('fu5ion/', Fu5ionPageView.as_view(), name="fu5ion"),
    # Path de Recorridos
    path('recorridos/', RecorridosPageView.as_view(), name="recorridos"),
]