from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MembroForm
from .models import Membro

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
# --- NOVA FUNÇÃO: LISTAR MEMBROS ---
def listar_membros(request):
    # Busca todos os membros e ordena pelo nome (A-Z)
    membros = Membro.objects.all().order_by('nome_completo')
    return render(request, 'membros/lista.html', {'membros': membros})