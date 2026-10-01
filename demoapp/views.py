from django.shortcuts import render, redirect
from .models import Zayavka
from .forms import CreateUserForm, CreateZayavkaForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    data = Zayavka.objects.filter(user=request.user)
    return render(request, 'index.html', context={
        'zayavki': data
    })

def register(request):
    if (request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/')
    else: 
        form = CreateUserForm()
    return render(request, 'register.html', context={
        'form': form 
    })

def create(request):
    if (request.method == 'POST'):
        form = CreateZayavkaForm(request.POST)
        if (form.is_valid()):
            newForm = form.save(commit=False)
            newForm.user = request.user
            newForm.save()
            return redirect('/')
    else:
        form = CreateZayavkaForm()
    return render(request, 'create.html', context={
            'form': form
        })
        