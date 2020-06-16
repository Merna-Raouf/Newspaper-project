from django.shortcuts import render
from home.models import *
# Create your views here.

def home(request):
    categories=Categoary.objects.all()
    if request.method == 'POST':
        categoary_id=request.POST.get("categoary_id")
        return render(request, 'AddArticle.html', {'categoary_id':categoary_id})
    else:
        return render(request, 'home.html', {'categories': categories})

def addnewCategoary(request):
    if request.method == 'POST':
        return render(request, 'AddCategoary.html')


def add_Categoary(request):
    if request.method == 'POST':
        categoary=Categoary()
        categoary.name=request.POST.get("name")
        categoary.save()
        return render(request, 'AddArticle.html', {'categoary_id':categoary.id})
    else:
        return render(request, 'AddCategoary.html')

def add_aricle(request):
    if request.method == 'POST':
        article=Article()
        article.Title = request.POST.get('title')
        article.Decription=request.POST.get('description')
        article.text = request.POST.get('paragraph')
        article.date = request.POST.get('date')
        article.writer=request.POST.get("writer")
        article.Article_image=request.POST.get("image")
        article.Article_Category_id=request.POST.get("categoary_id")
        article.save()
        return render(request, 'AddArticle.html', {'Categoary_id': article.Article_Category_id})
    else:
        return render(request, 'AddArticle.html')