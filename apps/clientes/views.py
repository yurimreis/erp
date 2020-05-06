from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ClientePessoaFisica
from .forms import ClientePessoaFisicaForm
from .entidades import cliente


# Função para retornar todos os clientes do banco
# O @login_required exige que o usuário esteja logado para acessar essa consulta
@login_required
def ListClientsPessoaFisica(request):
    list_clients_pf = ClientePessoaFisica.objects.all()
    data = {'list_clients_pf': list_clients_pf}
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
            client_new = cliente.ClientePessoaFisica(nome=nome, cpf=cpf, telefone=telefone, cep=cep,
                                                     logradouro=logradouro, numero=numero, complemento=complemento,
                                                     bairro=bairro, cidade=cidade, estado=estado)
            return redirect('list_clients')
    else:
        form = ClientePessoaFisicaForm()
    data = {'form': form}
    return render(request, 'clientes/form_client_pf.html', data)

# Função para editar um cliente pessoa física
# O @login_required exige que o usuário esteja logado para acessar essa consulta
@login_required
def EditClientPessoaFisica(request, id):
    edit_client = ClientePessoaFisica.objects.get(id=id)
    form = ClientePessoaFisicaForm(request.POST or None, instance=edit_client)
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
        client_new = cliente.ClientePessoaFisica(nome=nome, cpf=cpf, telefone=telefone, cep=cep,
                                                 logradouro=logradouro, numero=numero, complemento=complemento,
                                                 bairro=bairro, cidade=cidade, estado=estado)
        return redirect('list_clients')
    data = {'form': form}
    return render(request, 'clientes/form_client_pf.html', data)

@login_required
def DeleteClientPessoaFisica(request, id):
    client = ClientePessoaFisica.objects.get(id=id)
    if request.method == "POST":
        client.delete()
        return redirect('list_clients')
    data = {'client': client}
    return render(request, 'clientes/confirma_exclusao.html', data)