from django.urls import path

from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('viajeros', views.viajeros, name="Viajeros"),
    path('establecimientos', views.establecimientos, name="Establecimientos"),
    path('destinos', views.destinos, name="Destinos"), 
    path('buscar/', views.buscar),
   
]

