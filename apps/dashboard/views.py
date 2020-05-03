from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def clients(request):
    return render(request, 'dashboard/clientes.html')