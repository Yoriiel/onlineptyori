from .models import Links


def procesador(request): 
    contx = {}
    links = Links.objects.all()

    for link in links:
        contx[link.key] = link.url

    return contx

    


