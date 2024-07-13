from django.db import models
from django.contrib.auth.hashers import check_password as auth_check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group

# Create your models here.

class userManager(BaseUserManager):
    def create_user(self, nama ,email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        email = self.normalize_email(email)
        user = self.model(email=email, nama = nama)
        user.set_password(password)
        user.save(using = self.db)
        return user
    


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=150, unique=True)

    class Meta:
        managed = False
        db_table = 'users'
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama'] 
    
    objects = userManager()

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
    id_user = models.ForeignKey(Users,on_delete=models.CASCADE,db_column='id_user')
    id_game = models.ForeignKey(Games, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'detail_users'

