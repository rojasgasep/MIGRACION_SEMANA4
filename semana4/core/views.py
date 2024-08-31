from django.shortcuts import render

# Create your views here.

#funcion que retorna la vista del index, llamada en la linea 8 de urls.py
def index(request):
    return render(request, 'core/index.html')

def callofduty(request):
    return render(request, 'core/callofduty.html')

def accion(request):
    return render(request, 'core/accion.html')

def familiar(request):
    return render(request, 'core/familiar.html')

def deportes(request):
    return render(request, 'core/deportes.html')

def horror(request):
    return render(request, 'core/horror.html')

def rpg1(request):
    return render(request, 'core/rpg1.html')

def registro(request):
    return render(request, 'registro.html')

def baldursgate(request):
    return render(request, 'baldursgate.html')

def fallguys(request):
    return render(request, 'fallguys.html')

def godofwar(request):
    return render(request, 'godofwar.html')



