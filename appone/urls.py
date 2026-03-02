from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/items/', views.json_items, name='api-items'),
    path('all/math/fact/', views.math_fact, name='math-fact'),
    path('all/array/odd/', views.odd_numbers, name='odd-numbers'),
]