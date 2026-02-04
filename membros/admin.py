from django.contrib import admin
from .models import Membro

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    # --- LISTAGEM (TABELA) ---
    list_display = ('nome_completo', 'cargo', 'congregacao', 'telefone', 'situacao')
    list_display_links = ('nome_completo',)
    
    # CORREÇÃO PRINCIPAL AQUI:
    # Trocamos 'ativo' por 'situacao'
    list_filter = ('cargo', 'congregacao', 'situacao')
    
    search_fields = ('nome_completo', 'numero_ficha', 'cpf')
    list_per_page = 20

    # --- FORMULÁRIO DE CADASTRO ---
    fieldsets = (
        ('Identificação', {
            'fields': ('numero_ficha', 'foto', 'nome_completo', 'data_nascimento', 'cpf', 'rg', 'orgao_expedidor')
        }),
        ('Contato', {
            'fields': ('telefone', 'email', 'endereco', 'bairro', 'cidade', 'uf', 'cep')
        }),
        ('Vida Eclesiástica', {
            'fields': (
                'cargo', 
                'congregacao',
                'data_batismo_aguas',
                'data_batismo_espirito'
            )
        }),
        ('Dados Familiares', {
            'fields': ('estado_civil', 'nome_conjuge', 'nome_pai', 'nome_mae')
        }),
        ('Outros', {
            'fields': ('profissao', 'situacao', 'anotacoes', 'aceite_termos')
        }),
    )