from django.shortcuts import render
from .forms import FeedbackForm
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.shortcuts import render, redirect
def store(request):
    context = {}
    return render(request, 'app/store.html', context)

def pool(request):
    context = {}
    return render(request, 'app/pool.html', context)

def cart(request):
    context = {}
    return render(request, 'app/cart.html', context)

def contact(request):
    context = {}
    return render(request, 'app/contact.html', context)

def news(request):
    context = {}
    return render(request, 'app/news.html', context)

def catalog(request):
    context = {}
    return render(request, 'app/catalog.html', context)

def resurs(request):
    context = {}
    return render(request, 'app/resurs.html', context)

def pool(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'app/pool.html', {'data': data})
    else:
        form = FeedbackForm()
    return render(request, 'app/pool.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()
            return redirect('login')
    else:
        regform = UserCreationForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html', {'regform': regform, 'year': datetime.now().year, }
    )