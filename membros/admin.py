from django.contrib import admin
from django.utils.html import format_html
from .models import Membro

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    # --- LISTAGEM ---
    list_display = ('foto_pequena', 'nome_completo', 'cargo', 'congregacao', 'telefone', 'situacao')
    list_display_links = ('foto_pequena', 'nome_completo')
    list_filter = ('cargo', 'congregacao', 'situacao')
    search_fields = ('nome_completo', 'numero_ficha', 'cpf')
    list_per_page = 20

    # --- VISUALIZAÇÃO DA FOTO ---
    def foto_pequena(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%;" />', obj.foto.url)
        return "-"
    foto_pequena.short_description = "Foto"

    def foto_grande(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px; border-radius: 10px; box-shadow: 0px 0px 5px #ccc;" />', obj.foto.url)
        return "Nenhuma foto cadastrada"
    foto_grande.short_description = "Visualização da Foto"

    readonly_fields = ['foto_grande']

    # --- CONFIGURAÇÃO DO SCRIPT DE MÁSCARAS ---
    class Media:
        js = ('js/mascaras.js',)

    # --- ESTRUTURA DO FORMULÁRIO ---
    fieldsets = (
        ('Identificação', {
            'fields': (
                'numero_ficha', 
                'foto_grande',
                'foto', 
                'nome_completo', 
                'data_nascimento', 
                ('cpf', 'rg') 
            )
        }),
        ('Contato', {
            'fields': ('telefone', 'email', 'endereco', 'bairro', 'cidade', 'uf', 'cep')
        }),
        ('Vida Eclesiástica', {
            'fields': (
                'cargo', 
                'congregacao',
                'data_batismo_aguas',
                # Removido Batismo no Espirito Santo daqui
            )
        }),
        ('Dados Familiares', {
            'fields': ('estado_civil', 'nome_conjuge', 'nome_pai', 'nome_mae')
        }),
        ('Outros', {
            'fields': ('profissao', 'situacao', 'anotacoes', 'aceite_termos')
        }),
    )