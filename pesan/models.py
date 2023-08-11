from django.db import models

# Create your models here.


class Pesan(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField()
    pesan = models.CharField(max_length=250)
    waktu_posting = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return "{}.{}".format(self.nama, self.email)
