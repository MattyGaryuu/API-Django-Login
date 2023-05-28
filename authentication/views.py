from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,get_user_model,logout
from .models import CustomUser,UserFav


import authentication
# Create your views here.

def home(request):
    logado = False
    if request.user.is_authenticated:
        user_id = request.session.get('user_id')
        usuario = get_user_model().objects.get(ID=user_id)
        logado = True
        context = {
            'log' : logado,
            'usuario' : usuario,
            'id' : user_id
        }
    else:
        context = {
            'log' : logado,
            'usuario' : 'none',
            'id' : 0
        }
    return render(request,"index.html", context)


def signup(request):

    if request.method =="POST":
        usuario =  request.POST.get('Usuario')
        email = request.POST.get('email')
        senha1 = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        
        if senha1 != senha2:
            messages.error(request, 'As senhas não correspondem.')
            return redirect('home')

        user = get_user_model()
        user = user.objects.create_user(email=email,password=senha1,username=usuario)
        user.save()

        messages.success(request, "Sua conta foi criada com sucesso!")

        return redirect('signin')



    return render(request,"signup.html")

def signin(request):

    if request.method == "POST":
        usuario = request.POST.get('Usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username= usuario, password=senha)

        if usuario is not  None:
            request.session['user_id'] = user.ID
            login(request, user)
            return redirect('home')

        else:
            messages.error(request,"Usuário não encontrado")

            return redirect('home')


    return render(request,"signin.html")

def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect(home)

def fav(request, user_id):
    fav = UserFav.objects.filter(usuario_id=user_id)
    usuario = get_user_model().objects.get(ID=user_id).get_username
    context = {
        'fav':fav,
        'usuario': usuario
    }
    return render(request, "fav.html", context)

def addfav(request):
    logado = False
    if request.user.is_authenticated:
        logado = True
        if request.method == "POST":
            user_id = request.session.get('user_id')
            manga_id =  request.POST.get('Manga')
            
            manga = UserFav(id_manga=manga_id,usuario_id=user_id)
            manga.save()
            messages.success(request,"Item adicionado com sucesso")
        
    return render(request, "addfav.html", {'log':logado})

