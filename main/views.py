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

def planet_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    planets = Planet.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, 
                                     slug=category_slug)
        planets = Planet.objects.filter(category=category)
    return render(request, 'main/product/list.html', {'category':category,
                                                      'categories': categories,
                                                      'planets': planets})

                                    

