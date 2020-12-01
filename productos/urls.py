from django.urls import path
from. import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.listadeproductos, name='listadeproductos'),
    path('productos/', views.listadeproductos, name='listadeproductos') ,
    path('producto/', views.producto, name='producto'),
]
