from django.shortcuts import render , redirect
from django.http import HttpResponse
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