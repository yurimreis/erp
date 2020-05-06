from django.urls import path
from .views import *


# URL's de acesso da app cliente
urlpatterns = [
    path('', ListClientsPessoaFisica, name='list_clients'),
    path('new', CreateClientsPessoaFisica, name='create_clients'),

]