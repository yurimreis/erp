from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ClientePessoaFisica
from .forms import ClientePessoaFisicaForm


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
            form.save()
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
    data = {'form': form}
    return render(request, 'clientes/form_client_pf.html', data)