from django.urls import path
from . import views


urlpatterns = [
    path('', views.popular_list, name='popular_list'), 
    path('<slug:planet_slug>/', views.planet_detail, name='planet_detail')
]
