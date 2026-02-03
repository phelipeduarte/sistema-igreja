from django.db import models  # <--- CORRIGIDO AQUI (era 'om')
from datetime import date

class Membro(models.Model):
    # --- 1. Nº (Controle Interno) ---
    # Certifique-se que esta linha NÃO tem '...' dentro dos parênteses
    numero_ficha = models.PositiveIntegerField(unique=True, verbose_name="Nº da Ficha", help_text="Número de identificação na igreja")
    
    # FOTO
    foto = models.ImageField(upload_to='fotos_membros/', blank=True, null=True, verbose_name="Foto do Membro")

    # ... resto do código ...
    # --- 2. DADOS PESSOAIS ---
    nome_completo = models.CharField(max_length=200)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    naturalidade = models.CharField(max_length=100, help_text="Cidade/Estado", blank=True, null=True)
    
    # Documentos
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    rg = models.CharField(max_length=20, verbose_name="RG", blank=True, null=True)
    orgao_expedidor = models.CharField(max_length=20, verbose_name="Órgão Exp.", blank=True, null=True)
    
    # Estado Civil
    ESTADO_CIVIL_CHOICES = [
        ('SOLTEIRO', 'Solteiro(a)'),
        ('CASADO', 'Casado(a)'),
        ('VIUVO', 'Viúvo(a)'),
        ('DIVORCIADO', 'Divorciado(a)'),
    ]
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES)
    
    profissao = models.CharField(max_length=100, verbose_name="Profissão", blank=True, null=True)
    
    # Filiação
    nome_pai = models.CharField(max_length=200, verbose_name="Nome do Pai", blank=True, null=True)
    nome_mae = models.CharField(max_length=200, verbose_name="Nome da Mãe", blank=True, null=True)

    # --- 2. ENDEREÇO E CONTATO ---
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    numero = models.CharField(max_length=20, verbose_name="Nº")
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=9, verbose_name="CEP")
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, verbose_name="UF", default='RJ') # Mudei para RJ conforme sua ficha
    
    telefone = models.CharField(max_length=20, verbose_name="Celular/WhatsApp")
    email = models.EmailField(blank=True, null=True)

    # --- 3. DADOS ECLESIÁSTICOS ---
    data_batismo_aguas = models.DateField(verbose_name="Batismo nas Águas", blank=True, null=True)
    data_batismo_espirito = models.DateField(verbose_name="Batismo no Espírito Santo", blank=True, null=True)
    
    CARGO_CHOICES = [
        ('MEMBRO', 'Membro'),
        ('AUXILIAR', 'Auxiliar'),
        ('DIACONO', 'Diácono'),
        ('PRESBITERO', 'Presbítero'),
        ('EVANGELISTA', 'Evangelista'),
        ('PASTOR', 'Pastor'),
        ('OUTRO', 'Outro'),
    ]
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES, default='MEMBRO')
    cargo_outro = models.CharField(max_length=50, blank=True, null=True, help_text="Preencher se escolheu 'Outro'")
    
    igreja_procedencia = models.CharField(max_length=150, verbose_name="Igreja de Procedência", blank=True, null=True)

    # --- LISTA DE CONGREGAÇÕES ---
    CONGREGACAO_CHOICES = [
        ('Matriz em Piabetá', 'Matriz em Piabetá'),
        ('Jardim Prainha', 'Jardim Prainha'),
        ('Jardim Ana Beatriz', 'Jardim Ana Beatriz'),
        ('Parque Santana', 'Parque Santana'),
        ('Parque Veneza', 'Parque Veneza'),
        ('Rua das Mangueiras', 'Rua das Mangueiras'),
        ('Saracuruna', 'Saracuruna'),
        ('Avenida Mauá', 'Avenida Mauá'),
        ('Fragoso', 'Fragoso'),
        ('Meio da Serra', 'Meio da Serra'),
        ('Pau Grande', 'Pau Grande'),
        ('Jardim Nazareno', 'Jardim Nazareno'),
        ('Parque Sayonara', 'Parque Sayonara'),
        ('Vila Serrana / Ilha', 'Vila Serrana / Ilha'),
        ('Cachoeira Grande', 'Cachoeira Grande'),
        ('Boa Esperança', 'Boa Esperança'),
        ('Figueira Conceição', 'Figueira Conceição'),
        ('Rio do Ouro', 'Rio do Ouro'),
        ('Rio Novo', 'Rio Novo'),
        ('Suruí', 'Suruí'),
        ('Cidade Naval', 'Cidade Naval'),
        ('Figueira Magé', 'Figueira Magé'),
        ('Itambi / Mauá', 'Itambi / Mauá'),
        ('Leque Azul', 'Leque Azul'),
        ('Santa Dalila', 'Santa Dalila'),
        ('Ypiranga', 'Ypiranga'),
        ('Paraíso do Góia', 'Paraíso do Góia'),
        ('Bacaxá / Vila Canaã', 'Bacaxá / Vila Canaã'),
        ('Bananeiras / Água', 'Bananeiras / Água'),
        ('Fazendinha Branca', 'Fazendinha Branca'),
        ('Bonsucesso', 'Bonsucesso'),
        ('Praia Seca / Raia', 'Praia Seca / Raia'),
        ('Macaé / Itatiquara', 'Macaé / Itatiquara'),
        ('Parque Cidade Luz', 'Parque Cidade Luz'),
        ('Betel / Bereia', 'Betel / Bereia'),
        ('Filadelfia / Imburi', 'Filadelfia / Imburi'),
        ('Eldorado', 'Eldorado'),
        ('Parque Nova Campos', 'Parque Nova Campos'),
        ('Parque Prazeres', 'Parque Prazeres'),
        ('Vila Menezes', 'Vila Menezes'),
    ]
    congregacao = models.CharField(
        max_length=100, 
        choices=CONGREGACAO_CHOICES, 
        verbose_name="Congregação", 
        default='Matriz em Piabetá'
    )

    # --- 4. DADOS FAMILIARES (Cônjuge) ---
    nome_conjuge = models.CharField(max_length=200, verbose_name="Nome do Cônjuge", blank=True, null=True)

    # --- 4. ANOTAÇÕES ---
    anotacoes = models.TextField(verbose_name="Anotações", blank=True, null=True)

    # --- CONTROLE DO SISTEMA ---
    aceite_termos = models.BooleanField(default=False, verbose_name="Aceito os termos de uso de dados")
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero_ficha} - {self.nome_completo}"

# Classe Filho continua igual...
class Filho(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='filhos')
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    
    @property
    def idade(self):
        if self.data_nascimento:
            today = date.today()
            return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return "N/A"

    def __str__(self):
        return self.nome