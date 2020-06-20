from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
url(r'^logout/$', views.homepage, name='homepage'),
    url(r'^accounts/profile/$', views.home, name='home'),
    url(r'^AddArticle$', views.add_aricle, name='AddArticle'),
    url(r'^AddnewCategoary$', views.addnewCategoary, name='AddnewCategoary'),
    url(r'^AddCategoary$', views.add_Categoary, name='AddCategoary'),
    url('^signup$', views.signup, name='signup'),
    url('', include('django.contrib.auth.urls')),
    url('admin/', admin.site.urls),
    url('^openArticle$', views.open_aricle, name='openArticle'),
    url('^EditArticle$', views.Edit_article, name='EditArticle'),
    url('^viewArticle$', views.view_aricle, name='viewArticle'),

]
