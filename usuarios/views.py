from django.shortcuts import render, redirect
from .models import MyFile
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        return render(request, "home/home.html")
    elif request.method == 'POST':
        file = request.FILES.get("my_file")

        if file:
            # Salvar o arquivo usando o modelo MyFile
            mf = MyFile(title="minha_imagem", archive=file) 
            mf.save()

            # Adicionar uma mensagem de sucesso
            messages.success(request, f'Arquivo "{file.name}" enviado com sucesso.')

            # Redirecionar para outra página ou para a mesma página
            return redirect('home')  # Substitua 'nome_da_view' pelo nome da view que você deseja redirecionar

        else:
            # Adicionar uma mensagem de erro
            messages.error(request, 'Nenhum arquivo enviado.')

            # Redirecionar para outra página ou para a mesma página
            return redirect('home')  # Substitua 'nome_da_view' pelo nome da view que você deseja redirecionar

    return HttpResponse("Método não suportado.")
