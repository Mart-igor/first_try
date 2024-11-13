from django.urls import path
from . import views


urlpatterns = [
    path('', views.popular_list, name='popular_list'), 
    path('shop/', views.planet_list, name='planet_list'),
    path('shop/category/<slug:category_slug>/', views.planet_list, name='planet_list_by_cat'),
    path('<slug:planet_slug>/', views.planet_detail, name='planet_detail'),
]
