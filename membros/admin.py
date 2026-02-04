from django.contrib import admin
from django.utils.html import format_html
from django.forms import TextInput # <--- Importante para ajustar a caixa
from .models import Membro

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    # --- LISTAGEM ---
    list_display = ('foto_pequena', 'numero_ficha', 'numero_ficha_antiga', 'nome_completo', 'congregacao', 'situacao')
    list_display_links = ('foto_pequena', 'nome_completo')
    list_filter = ('cargo', 'congregacao', 'situacao')
    search_fields = ('nome_completo', 'numero_ficha', 'numero_ficha_antiga', 'cpf')
    list_per_page = 20
    ordering = ('numero_ficha',)

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

    readonly_fields = ['foto_grande', 'numero_ficha']

    class Media:
        js = ('js/mascaras.js',)

    # --- AJUSTE VISUAL DA CAIXA PEQUENA ---
    def formfield_for_dbfield(self, db_field, **kwargs):
        # Se for o campo da ficha antiga, força ele a ser pequeno
        if db_field.name == 'numero_ficha_antiga':
            kwargs['widget'] = TextInput(attrs={'style': 'width: 80px;', 'placeholder': '00000'})
        return super().formfield_for_dbfield(db_field, **kwargs)

    # --- ESTRUTURA DO FORMULÁRIO ---
    fieldsets = (
        ('Identificação', {
            'fields': (
                ('numero_ficha', 'numero_ficha_antiga'), # Coloquei lado a lado
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
            )
        }),
        ('Dados Familiares', {
            'fields': ('estado_civil', 'nome_conjuge', 'nome_pai', 'nome_mae')
        }),
        ('Outros', {
            'fields': ('profissao', 'situacao', 'anotacoes')
        }),
    )