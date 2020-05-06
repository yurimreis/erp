from django import forms
from .models import ClientePessoaFisica


class ClientePessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = ClientePessoaFisica
        fields = ['nome', 'cpf', 'telefone', 'cep', 'logradouro', 'numero',
                  'complemento', 'bairro', 'cidade', 'estado']