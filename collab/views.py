from django.shortcuts import render, redirect
from collab.forms import *
from collab.models import *
from django.contrib import messages
# Create your views here.


def sign_collaboratree(request):
    titlenya = "Collaboratree"
    konteks = {
        'title': titlenya,
    }

    if request.POST:
        collab = FormCollab(request.POST)
        if collab.is_valid():
            collab.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            collab = FormCollab()
            konteks['collab'] = collab
            return render(request, 'sign_collaboratree.html', konteks)
    else:
        collab = FormCollab()
        konteks['collab'] = collab

    return render(request, 'sign_collaboratree.html', konteks)


def ubah_collab(request, id_collab):
    titlenya = "Ubah Collab"

    collabs = Collab.objects.get(id=id_collab)
    if request.POST:
        collab = FormCollab(request.POST, instance=collabs)
        if collab.is_valid():
            collab.save()
            messages.success(request, "Data Berhasil diubah")
            return redirect('ubah_collab', id_collab=id_collab)
    else:
        collab = FormCollab(instance=collabs)
        konteks = {
            'collab': collab,
            'collabs': collabs,
            'title': titlenya,
        }
    return render(request, 'ubah_collab.html', konteks)


def Collab_View(request):
    titlenya = "Daftar Collaboratree"
    collabs = Collab.objects.all()

    konteks = {
        'collabs': collabs,
        'title': titlenya,
    }
    return render(request, 'tampil_collab.html', konteks)


def hapus_collab(request, id_collab):
    collabs = Collab.objects.filter(id=id_collab)
    collabs.delete()
    messages.success(request, "Data Terhapus")
    return redirect('/Vcollab')
