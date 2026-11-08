from django.shortcuts import render

def accueil(request):
    return render(request, 'quartiers/accueil.html')

def a_propos(request):
    return render(request, 'quartiers/apropos.html')

def lieux(request):
    lieux_list = [
        {"nom": "Marché Tilène", "cat": "Marché", "desc": "Le cœur de la Médina.", "img": "images/tilene.jpeg"},
        {"nom": "Marché Colobane", "cat": "Marché", "desc": "La plus grande friperie.", "img": "images/colobane.jpeg"},
        {"nom": "Plage de Yoff", "cat": "Plage", "desc": "Pirogues des pêcheurs Lébous.", "img": "images/yoff.jpeg"},
        {"nom": "Île de Ngor", "cat": "Plage", "desc": "Eau turquoise et surf.", "img": "images/ngor-plage.jpeg"},
        {"nom": "Corniche & Mosquée", "cat": "Corniche", "desc": "Mosquée de la Divinité.", "img": "images/corniche.jpeg"},
        {"nom": "Monument Renaissance", "cat": "Monument", "desc": "52m de bronze.", "img": "images/renaissance.jpeg"},
        {"nom": "Musée des Civilisations Noires", "cat": "Musée", "desc": "Histoire de l'Afrique.", "img": "images/musee.jpeg"},
        {"nom": "Corniche", "cat": "Corniche", "desc": "Coucher de soleil.", "img": "images/corniche-ouest.jpeg"},
    ]
    return render(request, 'quartiers/lieux.html', {"lieux": lieux_list})

def histoires(request):
    return render(request, 'quartiers/histoires.html')

def loisirs(request):
    return render(request, 'quartiers/loisirs.html')