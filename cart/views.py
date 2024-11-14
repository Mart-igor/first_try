from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Planet
from .cart import Cart
from .forms import CartAddPlanet


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    planet = get_object_or_404(Planet, id=product_id)
    form = CartAddPlanet(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=planet,
                 quantity=cd['quantity'], 
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    planet = get_object_or_404(Planet, id=product_id)
    cart.remove(planet)
    return redirect('cart:cart_deatil')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/datail.hmtl', {'cart':cart})

# Create your views here.
