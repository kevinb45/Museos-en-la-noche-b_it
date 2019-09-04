from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.photo.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nombre", max_length=25)
    surname = models.CharField(verbose_name="Apellido", max_length=25)
    telephone = models.CharField(verbose_name="Teléfono", null=True, blank=True, max_length=20)
    nationality = models.CharField(verbose_name="Nacionalidad", max_length=25, null=True, blank=True)
    photo = models.ImageField(upload_to=custom_upload_to, verbose_name="Foto", null=True, blank=True)   

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance,  **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print("Se acaba de crear un usuario y su perfil enlazado")