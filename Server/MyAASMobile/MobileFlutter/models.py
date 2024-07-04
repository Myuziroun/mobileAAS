from django.db import models


class Pengguna(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'pengguna'



class detailPengguna(models.Model):
    id_detailpengguna = models.AutoField(primary_key=True)
    id_pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    total_dzikir = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'detail_pengguna'

