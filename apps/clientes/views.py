from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ClientePessoaFisica
from .forms import ClientePessoaFisicaForm
from .entidades import cliente
from .services import cliente_pf_service

# Função para retornar todos os clientes do banco
# O @login_required exige que o usuário esteja logado para acessar essa consulta
@login_required
def ListClientsPessoaFisica(request):
    clientes = cliente_pf_service.listar_clientes()
    data = {'list_clients_pf': clientes}
    return render(request, 'clientes/clientes.html', data)

# Função para cadastrar um cliente pessoa física e posteriormente redirecionando ele para a lista de clientes
# O @login_required exige que o usuário esteja logado para acessar essa consulta
@login_required
def CreateClientsPessoaFisica(request):
    if request.method == "POST":
        form = ClientePessoaFisicaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            cpf = form.cleaned_data["cpf"]
            telefone = form.cleaned_data["telefone"]
            cep = form.cleaned_data["cep"]
            logradouro = form.cleaned_data["logradouro"]
            numero = form.cleaned_data["numero"]
            complemento = form.cleaned_data["complemento"]
            bairro = form.cleaned_data["bairro"]
            cidade = form.cleaned_data["cidade"]
            estado = form.cleaned_data["estado"]
            cliente_novo = cliente.ClientePessoaFisica(nome=nome, cpf=cpf, telefone=telefone, cep=cep,
                                                     logradouro=logradouro, numero=numero, complemento=complemento,
                                                     bairro=bairro, cidade=cidade, estado=estado)
            cliente_pf_service.cadastrar_cliente(cliente_novo)
            return redirect('list_clients')
    else:
        form = ClientePessoaFisicaForm()
    data = {'form': form}
    return render(request, 'clientes/form_client_pf.html', data)

# Função para editar um cliente pessoa física
# O @login_required exige que o usuário esteja logado para acessar essa consulta
@login_required
def EditClientPessoaFisica(request, id):
    cliente_antigo = cliente_pf_service.listar_cliente_id(id)
    form = ClientePessoaFisicaForm(request.POST or None, instance=cliente_antigo)
    if form.is_valid():
        nome = form.cleaned_data["nome"]
        cpf = form.cleaned_data["cpf"]
        telefone = form.cleaned_data["telefone"]
        cep = form.cleaned_data["cep"]
        logradouro = form.cleaned_data["logradouro"]
        numero = form.cleaned_data["numero"]
        complemento = form.cleaned_data["complemento"]
        bairro = form.cleaned_data["bairro"]
        cidade = form.cleaned_data["cidade"]
        estado = form.cleaned_data["estado"]
        cliente_novo = cliente.ClientePessoaFisica(nome=nome, cpf=cpf, telefone=telefone, cep=cep,
                                                 logradouro=logradouro, numero=numero, complemento=complemento,
                                                 bairro=bairro, cidade=cidade, estado=estado)
        cliente_pf_service.editar_cliente(cliente_antigo, cliente_novo)
        return redirect('list_clients')
    data = {'form': form}
    return render(request, 'clientes/form_client_pf.html', data)

@login_required
def DeleteClientPessoaFisica(request, id):
    cliente = cliente_pf_service.listar_cliente_id(id)
    if request.method == "POST":
        cliente_pf_service.remover_cliente(cliente)
        return redirect('list_clients')
    data = {'client': cliente}
    return render(request, 'clientes/confirma_exclusao.html', data)