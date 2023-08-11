from django.contrib import admin
from .models import Pesan
# Register your models here.

class kolomPesan(admin.ModelAdmin):
    list_display = ['id', 'nama', 'email', 'pesan', 'waktu_posting']
    search_fields = ['id', 'nama', 'email']
    list_filter = ['email']
    list_per_page = 5

admin.site.register(Pesan, kolomPesan)
