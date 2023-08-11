from django.contrib import admin
from .models import *
# Register your models here.


class kolomCollab(admin.ModelAdmin):
    list_display = ['id', 'email', 'nama', 'nomor', 'brand',
                    'tentang', 'bentuk_id', 'jumlah_id', 'waktu_posting']
    search_fields = ['id', 'brand', 'bentuk_id', 'jumlah_id']
    list_filter = ('bentuk_id', 'jumlah_id')
    list_per_page = 10


admin.site.register(Collab, kolomCollab)
admin.site.register(Bentuk)
admin.site.register(Jumlah)
