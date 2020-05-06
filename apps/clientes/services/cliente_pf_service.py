from ..models import ClientePessoaFisica


def listar_clientes():
    clientes = ClientePessoaFisica.objects.all()
    return clientes

def listar_cliente_id(id):
    cliente = ClientePessoaFisica.objects.get(id=id)
    return cliente

def remover_cliente(cliente):
    cliente.delete()

def cadastrar_cliente(cliente):
    ClientePessoaFisica.objects.create(nome=cliente.nome, cpf=cliente.cpf, telefone=cliente.telefone,
                                       cep=cliente.cep, logradouro=cliente.logradouro, numero=cliente.numero,
                                       complemento=cliente.complemento, bairro=cliente.bairro,
                                       cidade=cliente.cidade, estado=cliente.estado)

def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.cpf = cliente_novo.cpf
    cliente.telefone = cliente_novo.telefone
    cliente.cep = cliente_novo.cep
    cliente.logradouro = cliente_novo.logradouro
    cliente.numero = cliente_novo.numero
    cliente.complemento = cliente_novo.complemento
    cliente.bairro = cliente_novo.bairro
    cliente.cidade = cliente_novo.cidade
    cliente.estado = cliente_novo.estado
    cliente.save(force_update=True)