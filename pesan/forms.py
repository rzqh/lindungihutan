from django.forms import ModelForm
from pesan.models import Pesan
from django import forms


class FormPesan(ModelForm):
    nama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Nama'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 
                           'placeholder': 'Email'}))
    pesan = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 
                           'placeholder': 'Pesan'}))

    class Meta:
        model = Pesan
        fields = '__all__'

        # widgets = {
        #     'nama': forms.TextInput({'class':'form-control'}),
        #     'email': forms.EmailInput({'class':'form-control'}),
        #     'pesan': forms.Textarea({'class':'form-control'}),
        # }
