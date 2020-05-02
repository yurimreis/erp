from django.db import models


class ClientePessoaFisica(models.Model):

    # Dados básicos para emissão de NFe do cliente pessoa física (consumidor final)
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, null=False)
    telefone = models.CharField(max_length=11, null=True)
    cep = models.CharField(max_length=8, null=False)
    logradouro = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    complemento = models.CharField(max_length=50, null=True)
    bairro = models.CharField(max_length=50, null=False)
    cidade = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=2, null=False)

    # Função que retorna o nome do cliente
    def __str__(self):
        return self.nome