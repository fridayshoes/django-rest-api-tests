from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


urlpatterns = [
    path('apptwoapi/endpoint1/', views.app_two_view1, name='app-two-view1'),
    path('apptwoapi/endpoint2/', views.app_two_view2, name='app-two-view2'),
    path('apptwoapi/endpoint3/', views.app_two_view3, name='app-two-view3'),
]