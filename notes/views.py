from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Notedb
# Create your views here.

def home(request):
  notes = Notedb.objects.all()
  return render(request,"homepage.html",{"notes" : notes})

def add_note(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')

    Notedb.objects.create(
      title=title,
      content=content
    )
    return redirect("/")
  
  return render(request,'addnote.html')

def delete_note(request,id):
  note = Notedb.objects.get(id=id)
  note.delete()
  return redirect('/')

def update_note(request,id):
  note = Notedb.objects.get(id=id)

  if request.method == 'POST':
    note.title = request.POST.get('title')
    note.content = request.POST.get('content')
    note.save()   
    return redirect("/")
  
  return render(request,'updatenote.html',{"note":note})

def signup_view(request):

  if request.method == 'POST' :

    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    User.objects.create_user(
        username = username,
        password = password,
        email = email
    )

    return redirect('login')
  
  return render(request,'signup.html')

def login_view(request):
  
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(
      request,
      username = username,
      password = password
    )
    print(user)

    if user is not None :
      login(request,user)
      return redirect('home')
    
  return render(request ,'login.html')

def logout_view(request):
  logout(request)

  return redirect('login')