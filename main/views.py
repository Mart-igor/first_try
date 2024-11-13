from django.shortcuts import render, get_object_or_404
from models import Planet, Category


def popular_list(request):
    planets = Planet.objects.filter(available=True)[:3]
    return render(request, 
                  'main/index/index.html', 
                  {'planets': planets})

def planet_detail(request, planet_slug):
    planet = get_object_or_404(Planet, 
                               slug=planet_slug, 
                               available=True)
    return render(request, 
                  'main/product/detail.html',
                  {'planet':planet})

