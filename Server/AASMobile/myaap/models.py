from django.db import models
from django.contrib.auth.hashers import check_password as auth_check_password

# Create your models here.
class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'users'
    
    def check_password(self, raw_password):
        return auth_check_password(raw_password, self.password)
    @property
    def id(self):
        return self.id_user

class Games(models.Model):
    id_game = models.AutoField(primary_key=True)
    nama_game = models.CharField(max_length=100)
    genre_game = models.CharField(max_length=100)
    images_game = models.BinaryField()
    descriptions_game = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'games'

class detail_user(models.Model):
    id_detail_user = models.AutoField(primary_key=True)
    id_users = models.ForeignKey(Users,on_delete=models.CASCADE)
    id_game = models.ForeignKey(Games, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'detail_users'

