from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.timezone import now
from django_extensions.db.models import TimeStampedModel

class Actividades(models.Model):

    TIME_CHOICES = (('00:00', 'Medianoche'),
                    ('01:00', '01:00 AM'),
                    ('02:00', '02:00 AM'),
                    ('03:00', '03:00 AM'),
                    ('04:00', '04:00 AM'),
                    ('05:00', '05:00 AM'),
                    ('06:00', '06:00 AM'),
                    ('07:00', '07:00 AM'),
                    ('08:00', '08:00 AM'),
                    ('09:00', '09:00 AM'),
                    ('10:00', '10:00 AM'),
                    ('11:00', '11:00 AM'),
                    ('12:00', 'Mediodia'),
                    ('13:00', '01:00 PM'),
                    ('14:00', '02:00 PM'),
                    ('15:00', '03:00 PM'),
                    ('16:00', '04:00 PM'),
                    ('17:00', '05:00 PM'),
                    ('18:00', '06:00 PM'),
                    ('19:00', '07:00 PM'),
                    ('20:00', '08:00 PM'),
                    ('21:00', '09:00 PM'),
                    ('22:00', '10:00 PM'),
                    ('23:00', '11:00 PM'), 
            )


    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Descripcion")
    opening_hour = models.CharField(verbose_name="Apertura",max_length=20, choices=TIME_CHOICES,null=False)
    close_hour = models.CharField(verbose_name="Cierre",max_length=20, choices=TIME_CHOICES,null=False)
    accesibilty = models.BooleanField(verbose_name="Para personas con discapacidad", default=False)
    created = models.DateTimeField(auto_now_add= True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Ediccion")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(verbose_name="Activo", default=True)

   
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['title','content']

    def __str__(self):
        return self.title
 
def custom_upload_to(instance, filename):
    return 'museos/' + filename



class Museo(models.Model):

    COLECCIONES = (
        ('ARTE', 'ARTE'),
        ('HISTORIA', 'HISTORIA'),
        ('ARQUEOLOGIA', 'ARQUEOLOGIA'), 
        ('ANTROPOLOGIA', 'ANTROPOLOGIA'), 
        ('CIENCIA', 'CIENCIA'),
        ('AGRICULTURA', 'AGRICULTURA')
    )

    BARRIOS = (
        ('AGUADA', 'AGUADA'),
        ('AIRES PUROS', 'AIRES PUROS'),
        ('BARRIO SUR', 'BARRIO SUR'),
        ('BUCEO', 'BUCEO'), 
        ('CARRASCO', 'CARRASCO'), 
        ('CENTRO', 'CENTRO'),
        ('CERRO', 'CERRO'),
        ('CIUDAD VIEJA', 'CIUDAD VIEJA'),
        ('CORDON', 'CORDON'),
        ('BARRIO CAPURRO', 'BARRIO CAPURRO'),
        ('LA UNION', 'LA UNION'),
        ('LEZICA', 'LEZICA'),
        ('MARONAS', 'MARONAS'),
        ('PALERMO', 'PALERMO'),
        ('PARQUE RODO', 'PARQUE RODO'),
        ('PENAROL', 'PENAROL'),
        ('POCITOS', 'POCITOS'),
        ('PUNTA GORDA', 'PUNTA GORDA'),
        ('PUNTA CARRETAS', 'PUNTA CARRETAS'),
        ('PEREZ CASTELLANOS', 'PEREZ CASTELLANOS'),
        ('SAYAGO', 'SAYAGO'),
        ('TRES CRUCES', 'TRES CRUCES')
    )

    TIME_CHOICES = (('00:00', 'Medianoche'),
                    ('01:00', '01:00 AM'),
                    ('02:00', '02:00 AM'),
                    ('03:00', '03:00 AM'),
                    ('04:00', '04:00 AM'),
                    ('05:00', '05:00 AM'),
                    ('06:00', '06:00 AM'),
                    ('07:00', '07:00 AM'),
                    ('08:00', '08:00 AM'),
                    ('09:00', '09:00 AM'),
                    ('10:00', '10:00 AM'),
                    ('11:00', '11:00 AM'),
                    ('12:00', 'Mediodia'),
                    ('13:00', '01:00 PM'),
                    ('14:00', '02:00 PM'),
                    ('15:00', '03:00 PM'),
                    ('16:00', '04:00 PM'),
                    ('17:00', '05:00 PM'),
                    ('18:00', '06:00 PM'),
                    ('19:00', '07:00 PM'),
                    ('20:00', '08:00 PM'),
                    ('21:00', '09:00 PM'),
                    ('22:00', '10:00 PM'),
                    ('23:00', '11:00 PM'), 
            )
    
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Descripcion")
    colection =   models.CharField(verbose_name="Colección",max_length=20, choices=COLECCIONES,null=False)

    address = models.CharField(verbose_name="Direccion", max_length=200)
    district =   models.CharField(verbose_name="Barrio",max_length=20, choices=BARRIOS,null=False)
    web = models.URLField(verbose_name="Página Web", max_length=200, null=True, blank=True)
    email = models.EmailField(verbose_name="Email", max_length=200, null=True, blank=True)
    telephone = models.CharField(verbose_name="Teléfono", null=True, blank=True, max_length=20)

    opening_hour = models.CharField(verbose_name="Apertura",max_length=20, choices=TIME_CHOICES,null=False)
    close_hour = models.CharField(verbose_name="Colección",max_length=20, choices=TIME_CHOICES,null=False)
    accesibilty = models.BooleanField(verbose_name=" Acceso para discapacitados", default=False)
    wifi = models.BooleanField(verbose_name="WIFI", default=False)
    coffee = models.BooleanField(verbose_name="Cafeteria", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    activities = models.ManyToManyField(Actividades, verbose_name="Lista de actividades",blank=True)
    active = models.BooleanField(verbose_name="Activo", default=True)
   
    photo1 = models.ImageField(upload_to=custom_upload_to, verbose_name="Foto 1", null=True, blank=True) 
    photo2 = models.ImageField(upload_to=custom_upload_to, verbose_name="Foto 2", null=True, blank=True) 
    photo3 = models.ImageField(upload_to=custom_upload_to, verbose_name="Foto 3", null=True, blank=True) 
    author = models.OneToOneField(User, verbose_name="Autor", on_delete=models.CASCADE, null=False, blank=False)
    
    class Meta:
        verbose_name = "museo"
        verbose_name_plural = "museos"
        ordering = ['title']

    def __str__(self):
        return self.title



