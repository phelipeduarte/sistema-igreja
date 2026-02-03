from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MembroForm

def cadastrar_membro(request):
    if request.method == 'POST':
        # Se o usuário clicou em "Salvar"
        form = MembroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membro cadastrado com sucesso!')
            return redirect('cadastrar_membro') # Limpa o formulário para o próximo
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os campos.')
    else:
        # Se o usuário está apenas entrando na página
        form = MembroForm()

    return render(request, 'membros/cadastro.html', {'form': form})