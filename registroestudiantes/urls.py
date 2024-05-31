from django.urls import path
from.import views
urlpatterns = [

path('', views.reg_estudiantes, name='ho'),
path('informacion', views.informacion, name='info'),
path('libros', views.libros, name='libro'),

]




