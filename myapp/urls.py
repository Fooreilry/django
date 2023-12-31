"""
URL configuration for labs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from . import views, forms
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.store, name="store"),
    path('pool', views.pool, name="pool"),
    path('cart', views.cart, name="cart"),
    path('contact', views.contact, name="contact"),
    path('news', views.news, name="news"),
    path('catalog', views.catalog, name="catalog"),
    path('resurs', views.resurs, name="resurs"),
    path('registration', views.registration, name="registration"),
    path('blog', views.blog, name="blog"),
    path('newpost/', views.newpost, name="newpost"),
    path('blogpost/<int:parametr>/', views.blogpost, name="blogpost"),
    path('videopost/', views.videopost, name="videopost"),
    path('login/',
         LoginView.as_view(
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context={
                 'title': 'Авторизация',
                 'year': datetime.now().year,
             },
             next_page='/',
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
