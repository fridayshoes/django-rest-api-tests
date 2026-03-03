from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appthreeapi/endpoint1/', views.app_three_view1, name='app-three-view1'),
    path('appthreeapi/endpoint2/', views.app_three_view2, name='app-three-view2'),
    path('appthreeapi/endpoint3/', views.app_three_view3, name='app-three-view3'),
]