from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse # <--- IMPORTANTE: Adicione esta linha no topo
from .models import Membro

admin.site.site_header = "Gestão Assembleia de Deus"
admin.site.site_title = "AD Piabetá"
admin.site.index_title = "Painel Administrativo"

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    # 1. ADICIONE 'botoes_acao' NO FINAL DA LISTA ABAIXO:
    list_display = ('foto_preview', 'nome_completo', 'cargo', 'congregacao', 'telefone', 'ativo_status', 'botoes_acao')
    
    list_display_links = ('foto_preview', 'nome_completo')
    
    # Os filtros aparecem como caixas no topo da lista no Jazzmin
    list_filter = ('cargo', 'congregacao', 'ativo')
    
    search_fields = ('nome_completo', 'cpf', 'numero_ficha')
    list_per_page = 20

    fieldsets = (
        ('Identificação', {
            'fields': (('foto', 'foto_preview_large'), 'numero_ficha', 'nome_completo', 'cpf', 'rg')
        }),
        ('Contato e Endereço', {
            'fields': ('telefone', 'email', 'naturalidade', 'endereco')
        }),
        ('Dados Eclesiásticos', {
            'fields': (('cargo', 'congregacao'), 'data_batismo_aguas', 'data_batismo_espirito'),
            'classes': ('collapse',),
        }),
        ('Outros', {
            'fields': ('estado_civil', 'profissao', 'ativo', 'anotacoes')
        }),
    )
    
    readonly_fields = ('foto_preview_large',)

    # --- FUNÇÕES VISUAIS ---

    def foto_preview(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;" />', obj.foto.url)
        return "Sem Foto"
    foto_preview.short_description = "Foto"

    def foto_preview_large(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px; border-radius: 10px;" />', obj.foto.url)
        return "Visualização"

    def ativo_status(self, obj):
        return obj.ativo
    ativo_status.boolean = True
    ativo_status.short_description = "Ativo"

    # --- 2. NOVA FUNÇÃO PARA OS BOTÕES (COLE ISTO NO FINAL) ---
    def botoes_acao(self, obj):
        # Cria o link para editar
        edit_url = reverse('admin:membros_membro_change', args=[obj.id])
        # Cria o link para excluir
        delete_url = reverse('admin:membros_membro_delete', args=[obj.id])
        
        # Desenha os botões usando ícones do FontAwesome (que o Jazzmin já tem)
        return format_html(
            '<a class="btn btn-info btn-sm" href="{}" title="Editar"><i class="fas fa-pen"></i></a> '
            '<a class="btn btn-danger btn-sm" href="{}" title="Excluir"><i class="fas fa-trash"></i></a>',
            edit_url, delete_url
        )
    botoes_acao.short_description = "Ações"
    botoes_acao.allow_tags = True