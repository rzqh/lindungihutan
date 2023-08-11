from django.forms import ModelForm
from collab.models import Collab
from django import forms

class FormCollab(ModelForm):
    class Meta:
        model = Collab
        fields = '__all__'

        widgets = {
            'email' : forms.EmailInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'nomor' : forms.NumberInput({'class':'form-control'}),
            'brand' : forms.TextInput({'class':'form-control'}),
            'tentang' : forms.Textarea({'class':'form-control'}),
            'bentuk_id' : forms.Select({'class':'form-control'}),            
            'jumlah_id' : forms.Select({'class':'form-control'})           
        }
