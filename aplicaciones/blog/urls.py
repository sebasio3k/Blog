from django.urls import path
from .views import home, generales, tecnologia, videojuegos, espacio, detallePost

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales, name='generales'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('videojuegos/', videojuegos, name='videojuegos'),
    path('espacio/', espacio, name='espacio'),
    path('post/<slug:slug>', detallePost, name='detalle_post'),

]
