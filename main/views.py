from django.shortcuts import render, get_object_or_404
from models import Planet, Category
from django.core.paginator import Paginator


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
    page = request.GET.get('page', 1)
    category = None
    categories = Category.objects.all()
    planets = Planet.objects.filter(available=True)
    paginator = Paginator(planets, 1)
    page_obj = paginator.page(int(page))
    if category_slug:
        category = get_object_or_404(Category, 
                                     slug=category_slug)
        planets = Planet.objects.filter(category=category)
        paginator = Paginator(planets, 1)
        page_obj = paginator.page(int(page))
    return render(request, 'main/product/list.html', {'category':category,
                                                      'categories': categories,
                                                      'planets': planets})

                                    

