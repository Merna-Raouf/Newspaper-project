from django.shortcuts import render,redirect
from home.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'


def homepage(request):
    articles=Article.objects.all()
    return render(request, 'base.html',{'articles':articles})


def home(request):
    categories=Categoary.objects.all()
    if request.method == 'POST':
        categoary_id=request.POST.get("categoary_id")
        categories = Categoary.objects.all()
       # return render(request, 'showArticles.html', {'articles':articles})
        return render(request, 'AddArticle.html', {'categoary_id':categoary_id,'categories': categories,'user':request.user})
    else:
        articles=Article.objects.filter(user=request.user)
        return render(request, 'home.html', {'categories': categories,'articles':articles})

def addnewCategoary(request):
    if request.method == 'POST':
        return render(request, 'AddCategoary.html')


def add_Categoary(request):
    if request.method == 'POST':
        categoary=Categoary()
        categoary.name=request.POST.get("name")

        categoary.save()
        articles = Article.objects.filter(user=request.user)
        user = request.user
        return render(request, 'home.html',{'articles':articles,'user':user})
    else:
        return render(request, 'AddCategoary.html')

def add_aricle(request):
    categories = Categoary.objects.all()
    if request.method == 'POST':

        article=Article()
        article.Title = request.POST.get('title')
        article.Description=request.POST.get('description')
        article.text = request.POST.get('paragraph')
        article.date = request.POST.get('date')
        article.Article_image=request.FILES["image"]
        article.Article_Category_id=request.POST['selectcategoary']
        article.user=request.user
        article.save()
        articles = Article.objects.filter(user=request.user)
        return render(request, 'home.html', {'Categoary_id': article.Article_Category_id,'categories':categories,'articles':articles})
    else:
        return render(request, 'AddArticle.html', {'categories': categories})

def Edit_article(request):
    categories = Categoary.objects.all()
    if request.method == 'POST':
        article_id=request.POST.get('id')
        article=Article.objects.get(id=article_id)
        article.Title= request.POST.get('title')
        article.Description = request.POST.get('description')
        article.text = request.POST.get('paragraph')
        article.date = request.POST.get('date')
        if len(request.FILES) != 0:
            article.Article_image=request.FILES["image"]
        article.Article_Category_id = request.POST['selectcategoary']
        article.user = request.user
        article.save()
        articles = Article.objects.filter(user=request.user)
        return render(request, 'home.html', {'Categoary_id': article.Article_Category_id, 'categories': categories, 'articles': articles})
    else:
        article_id = request.GET.get('id')
        article = Article.objects.filter(id=article_id)
        return render(request, 'EditArticle.html', {'categories': categories,'article':article})


def open_aricle(request):
    article_id = request.GET.get('id')
    article = Article.objects.filter(id=article_id)
    return render(request, 'OpenArticle.html',{'article':article})

    #elif 'Edit' in request.POST:
     #   return render(request, 'EditArticle.html',{'article':article,'categoaries':categoaries})


def view_aricle(request):
    articles=Article.objects.all()
    return render(request,'viewArticles.html',{'articles':articles})