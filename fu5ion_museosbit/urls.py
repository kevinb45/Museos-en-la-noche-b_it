"""fu5ion_museosbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from museos.urls import museos_patterns
from profiles.urls import profiles_patterns

urlpatterns = [
    path('', include('core.urls')),
    # Paths de Contacto
    path('contact/', include('contact.urls')),
    # Paths de Museos
    path('museos/', include(museos_patterns)),
    # Paths de Admin
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),    
    path('accounts/', include('registration.urls')),
    # Paths de Profiles
    path('profiles/', include(profiles_patterns)),
]

# Debug para que se vean las imágenes si el modo debug esta activo en settings.py.
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Titulos modificables para los templates de admin.
admin.site.site_header = "Museos en la Noche"
admin.site.index_title = "Panel de Administrador"
admin.site.site_title = "Museos en la Noche"
