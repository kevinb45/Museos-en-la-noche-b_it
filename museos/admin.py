from django.contrib import admin
from .models import Museo, Actividades

from import_export.admin import ImportExportModelAdmin

# Register your models here.

class MuseoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'content','address','district','colection')
    search_fields = ('title', 'content', 'address', 'district', 'accesibilty', 'wifi', 'coffee')
    list_per_page = 10

    readonly_fields = ('author',)

    def get_readonly_fields(self,request, obj=None):
        if request.user.is_superuser or request.user.groups.filter(name="Admin").exists():
            return ()
        else: 
            return ('author',)

    # Inyectamos nuestro fichero css
    class Media:
        fields = ('title', 'content', 'colection','address','district','web','email', 'telephone', 'opening_hour', 'close_hour', 'accesibilty', 'wifi', 'coffee')
        export_order = ('title', 'content', 'colection','address','district','web','email', 'telephone', 'opening_hour', 'close_hour', 'accesibilty', 'wifi', 'coffee')
        css = {
            'all': ('museos/css/custom_ckeditor.css')
        }   

class ActividadesAdmin(ImportExportModelAdmin):
    list_display = ('title', 'content')
    # Inyectamos nuestro fichero css
    class Media:
        fields = ('title', 'content', 'opening_hour ', 'close_hour', 'accesibilty')
        export_order = ('title', 'content', 'opening_hour ', 'close_hour', 'accesibilty')
        css = {
            'all': ('museos/css/custom_ckeditor.css',)
        }

admin.site.register(Museo, MuseoAdmin)
admin.site.register(Actividades, ActividadesAdmin)



