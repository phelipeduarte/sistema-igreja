from django import forms
from .models import Membro
import re

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = '__all__'
        
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'data_batismo_aguas': forms.DateInput(attrs={'type': 'date'}),
            'data_batismo_espirito': forms.DateInput(attrs={'type': 'date'}),
            'anotacoes': forms.Textarea(attrs={'rows': 3}),
            'congregacao': forms.Select(attrs={'class': 'form-select'}),
            'cargo': forms.Select(attrs={'class': 'form-select'}),
        }

    # --- VALIDAÇÃO DE CPF (O Algoritmo Mágico) ---
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        
        # 1. Remove tudo que não for número (pontos e traços)
        cpf = re.sub(r'[^0-9]', '', cpf)

        # 2. Verifica se tem 11 dígitos
        if len(cpf) != 11:
            raise forms.ValidationError("O CPF deve conter 11 dígitos.")

        # 3. Verifica se todos os números são iguais (ex: 111.111.111-11 é inválido mas passa no cálculo)
        if cpf == cpf[0] * 11:
            raise forms.ValidationError("CPF inválido (números repetidos).")

        # 4. Cálculo do 1º Dígito Verificador
        soma = 0
        peso = 10
        for i in range(9):
            soma += int(cpf[i]) * peso
            peso -= 1
        
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        
        if resto != int(cpf[9]):
            raise forms.ValidationError("CPF inválido.")

        # 5. Cálculo do 2º Dígito Verificador
        soma = 0
        peso = 11
        for i in range(10):
            soma += int(cpf[i]) * peso
            peso -= 1
            
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
            
        if resto != int(cpf[10]):
            raise forms.ValidationError("CPF inválido.")

        # Se passou por tudo, retorna o CPF limpo (só números) para o banco
        return cpf