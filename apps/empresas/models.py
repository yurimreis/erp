from django.db import models


class Empresa(models.Model):

    # Dados da Empresa Usuária do ERP
    cnpj = models.CharField(max_length=14, null=False)
    razao_social = models.CharField(max_length=100, null=False)
    fantasia = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    cep = models.CharField(max_length=8, null=False)
    logradouro = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    complemento = models.CharField(max_length=50, null=True)
    bairro = models.CharField(max_length=50, null=False)
    cidade = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=2, null=False)

    # Dados Fiscais da Empresa
    codigo_regime_tributario = models.CharField(max_length=1)
    regime_especial_de_tributacao = models.CharField(max_length=1)
    cnae = models.CharField(max_length=7)
    inscricao_municipal = models.CharField(max_length=10)
    inscricao_estadual = models.CharField(max_length=10)
    identificacao_csc = models.CharField(max_length=5)
    codigo_contribuinte = models.CharField(max_length=50)

    # Retorna o a razão social da empresa
    def __str__(self):
        return self.razao_social