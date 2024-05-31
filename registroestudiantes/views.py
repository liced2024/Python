from django.shortcuts import render, redirect
from .models import Alumno
from .forms import LibroForm



def reg_estudiantes(request):
    return render (request, 'home.html')

def informacion(request):
    return render (request, 'paginas/informacion.html')


def libros(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('info') 
    else:
        form = LibroForm()

    return render (request, 'paginas/libros.html', {'form': form})


