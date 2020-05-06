from django.urls import path
from .views import *


# URL's de acesso da app cliente
urlpatterns = [
    path('', ListClientsPessoaFisica, name='list_clients'),
    path('new', CreateClientsPessoaFisica, name='create_clients'),
    path('edit/<int:id>', EditClientPessoaFisica, name='edit_client'),
    path('delete/<int:id>', DeleteClientPessoaFisica, name='delete_client'),
]