from django.contrib import admin
from django.utils.html import format_html
from .models import Membro

# --- CONFIGURAÇÃO VISUAL DO SITE (Branding) ---
admin.site.site_header = "Gestão Assembleia de Deus"
admin.site.site_title = "AD Piabetá"
admin.site.index_title = "Painel Administrativo"

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    # 1. O que aparece na lista (Colunas)
    list_display = ('foto_preview', 'nome_completo', 'cargo', 'congregacao', 'telefone', 'ativo_status')
    
    # 2. Links para clicar e editar (Geralmente o nome)
    list_display_links = ('foto_preview', 'nome_completo')
    
    # 3. Filtros laterais (Barra direita)
    list_filter = ('cargo', 'congregacao', 'ativo')
    
    # 4. Campo de Busca (Lupa)
    search_fields = ('nome_completo', 'cpf', 'numero_ficha')
    
    # 5. Paginação (Quantos por página)
    list_per_page = 20

    # 6. Organização do Formulário de Edição (Agrupamento)
    fieldsets = (
        ('Identificação', {
            'fields': (('foto', 'foto_preview_large'), 'numero_ficha', 'nome_completo', 'cpf', 'rg')
        }),
        ('Contato e Endereço', {
            'fields': ('telefone', 'email', 'naturalidade', 'endereco')
        }),
        ('Dados Eclesiásticos', {
            'fields': (('cargo', 'congregacao'), 'data_batismo_aguas', 'data_batismo_espirito'),
            'classes': ('collapse',), # Deixa essa aba recolhível se quiser
        }),
        ('Outros', {
            'fields': ('estado_civil', 'profissao', 'ativo', 'anotacoes')
        }),
    )

    # Campos que não podem ser editados (apenas leitura)
    readonly_fields = ('foto_preview_large',)

    # --- FUNÇÕES AUXILIARES PARA MOSTRAR IMAGENS ---

    # Miniatura na Lista
    def foto_preview(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;" />', obj.foto.url)
        return "Sem Foto"
    foto_preview.short_description = "Foto"

    # Foto Grande no Formulário
    def foto_preview_large(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px; border-radius: 10px;" />', obj.foto.url)
        return "Sem Foto carregada"
    foto_preview_large.short_description = "Visualização da Foto Atual"

    # Status bonitinho (Ícone)
    def ativo_status(self, obj):
        return obj.ativo
    ativo_status.boolean = True # Transforma True/False em ícone de ✅/❌
    ativo_status.short_description = "Ativo"