from django.shortcuts import render
import random

def home(request):
    return render(request,'password/home.html')

def about(request):
    return render(request, 'password/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    length = request.GET.get('length',10)

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    if request.GET.get('special'):
        characters.extend('~!@#$%^&*()_+')

    for i in range(0,int(length)):
        password += random.choice(characters)

    return render(request, 'password/password.html', {'password':password})
