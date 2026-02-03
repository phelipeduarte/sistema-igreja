from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# 1. VERIFIQUE SE O 'excluir_membro' ESTÁ NESTA LINHA:
from membros.views import cadastrar_membro, listar_membros, editar_membro, excluir_membro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_membros, name='listar_membros'),
    path('cadastro/', cadastrar_membro, name='cadastrar_membro'),
    path('editar/<int:id>/', editar_membro, name='editar_membro'),
    
    # 2. VERIFIQUE SE ESTA LINHA EXISTE:
    path('excluir/<int:id>/', excluir_membro, name='excluir_membro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)