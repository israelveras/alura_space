from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import Fotografia


def index(request):
    if request.user.is_authenticated:
        fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")
        return render(request, 'galeria/index.html', {"cards": fotografias})
    else:
        messages.error(request, "Usuário não logado")
        return redirect('login')

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Para efetuar buscas, o usuário deve estar logado')
        return redirect('login')

    fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)



    return render(request, "galeria/buscar.html", {"cards": fotografias})