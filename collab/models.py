from django.db import models

# Create your models here.


class Bentuk(models.Model):
    bentuk = models.CharField(max_length=200)
    ket = models.TextField()

    def __str__(self):
        return self.bentuk


class Jumlah(models.Model):
    jumlah = models.CharField(max_length=200)
    ket = models.TextField()

    def __str__(self):
        return self.jumlah


class Collab(models.Model):
    email = models.EmailField()
    nama = models.CharField(max_length=50)
    nomor = models.IntegerField()
    brand = models.CharField(max_length=50)
    tentang = models.CharField(max_length=250)
    bentuk_id = models.ForeignKey(Bentuk, on_delete=models.CASCADE, null=True)
    jumlah_id = models.ForeignKey(Jumlah, on_delete=models.CASCADE, null=True)
    waktu_posting = models.DateTimeField(auto_now_add=True)

    def _str_(self) :
        return "{}.{}".format(self.email, self.brand)
