from django.contrib import admin
from .models import Link

# Registramos nuestros modelos aquí
# En este caso decidimos que la fecha de creación y de modificación sean solo lectura para los Admin.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

    def get_readonly_fields(self,request, obj=None):
        if request.user.groups.filter(name="Admin").exists():
            return ('key', 'name')
        else:
            return ('created','updated')

admin.site.register(Link, LinkAdmin)