"""
URL configuration for ssputs project.

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
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from pesan.views import *
from collab.views import *


def index(request):
    titlenya = "Beranda"
    konteks = {
        'title': titlenya,
    }
    return render(request, 'index.html', konteks)


def blog(request):
    titlenya = "Blog"
    konteks = {
        'title': titlenya,
    }
    return render(request, 'blog.html', konteks)


def collaboratree(request):
    titlenya = "Collaboratree"
    konteks = {
        'title': titlenya,
    }
    return render(request, 'collaboratree.html', konteks)

def about(request):
    titlenya = "Tentang Kami"
    konteks = {
        'title': titlenya,
    }
    return render(request, 'about.html', konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('blog/', blog, name='blog'),
    path('tentang-kami/', about, name='about'),

    # PESAN
    path('kontak/', contact, name='contact'),
    path('Vpsn/', Pesan_View, name="Daftar Pesan"),
    path('hapus_psn/<int:id_pesan>', hapus_psn, name='hapus_psn'),
    path('ubah_psn/<int:id_pesan>', ubah_psn, name='ubah_psn'),
    # END - PESAN
    # COLLABORATREE
    path('collaboratree/', collaboratree, name='collaboratree'),
    path('sign_collaboratree/', sign_collaboratree, name='sign_1collaboratree'),
    path('Vcollab/', Collab_View, name="Daftar Pesan"),
    path('hapus_collab/<int:id_collab>', hapus_collab, name='hapus_collab'),
    path('ubah_collab/<int:id_collab>', ubah_collab, name='ubah_collab'),
    # END - COLLABORATREE
]
