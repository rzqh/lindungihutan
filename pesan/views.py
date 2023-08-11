from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from pesan.forms import FormPesan
from pesan.models import Pesan
from django.contrib import messages

# Create your views here.



def contact(request):
    titlenya = "Kontak"
    konteks = {
        'title': titlenya,
    }

    if request.POST:
        pesan = FormPesan(request.POST)
        if pesan.is_valid():
            pesan.save()
            messages.success(request, "Pesan terkirim")
            pesan = FormPesan()
            konteks['pesan'] = pesan            
            return render(request, 'contact.html', konteks)
    else:
        pesan = FormPesan()
        konteks['pesan'] = pesan

    return render(request, 'contact.html', konteks)

def ubah_psn(request, id_pesan):
    titlenya = "Ubah Pesan"

    pesans = Pesan.objects.get(id=id_pesan)
    if request.POST:
        pesan = FormPesan(request.POST, instance=pesans)
        if pesan.is_valid():
            pesan.save()
            messages.success(request, "Data Berhasil diubah")
            return redirect('ubah_psn', id_pesan=id_pesan)
    else:
        pesan = FormPesan(instance=pesans)
        konteks = {
            'pesan': pesan,
            'pesans': pesans,
            'title': titlenya,
        }
    return render(request, 'ubah_psn.html', konteks)


def Pesan_View(requset):
    titlenya = "Daftar Pesan"
    pesans = Pesan.objects.all()

    konteks = {
        'pesans': pesans,
        'title': titlenya
    }
    return render(requset, 'tampil_pesan.html', konteks)

def hapus_psn(request, id_pesan):
    pesans = Pesan.objects.filter(id=id_pesan)
    pesans.delete()
    messages.success(request, "Data Terhapus")
    return redirect('/Vpsn')

