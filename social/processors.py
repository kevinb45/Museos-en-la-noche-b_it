# Importamos de models Link para poder utilizar el diccionario de contexto
# para vincular con redes sociales en la base de nuestro template.
from .models import Link


# Creamos diccionario
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    # Recorremos los links
    for link in links:
        ctx[link.key] = link.url
    return ctx