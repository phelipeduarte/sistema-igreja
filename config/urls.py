from membros.views import cadastrar_membro, listar_membros, editar_membro
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# IMPORTANTE: Adicione listar_membros aqui
from membros.views import cadastrar_membro, listar_membros

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota do Cadastro
    path('cadastro/', cadastrar_membro, name='cadastrar_membro'),
    
    # --- ROTA DA PÁGINA INICIAL (HOME) ---
    # As aspas vazias '' significam "raiz do site"
    path('', listar_membros, name='listar_membros'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_membros, name='listar_membros'),
    path('cadastro/', cadastrar_membro, name='cadastrar_membro'),

    # NOVA ROTA DE EDIÇÃO (com ID)
    path('editar/<int:id>/', editar_membro, name='editar_membro'),
]