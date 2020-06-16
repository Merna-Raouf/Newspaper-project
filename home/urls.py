from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),

    url(r'^AddArticle$', views.add_aricle, name='AddArticle'),
    url(r'^AddnewCategoary$', views.addnewCategoary, name='AddnewCategoary'),
url(r'^AddCategoary$', views.add_Categoary, name='AddCategoary'),
]