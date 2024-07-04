import base64
from rest_framework import serializers
from .models import Users, Games, detail_user
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

# User = get_user_model()   

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
class GamesModelSerializer(serializers.ModelSerializer):
    # gambar_game_base64 = serializers.SerializerMethodField()
    class Meta:
        model = Games
        fields = '__all__'
        
    # def get_gambar_game_base64(self, obj):
    #     if obj.images_game:
    #         return base64.b64encode(obj.images_game).decode('utf-8')
    #     return None
class detailUsersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = detail_user
        fields = '__all__'

class UserRegistrasiModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ('nama','email','password')
    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        return user

from rest_framework import serializers
from .models import Users

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = Users.objects.get(email=email, password=password)
                # Jika user ditemukan, return validated data
                data['users'] = user
            except Users.DoesNotExist:
                raise serializers.ValidationError("Email atau password salah")
        else:
            raise serializers.ValidationError("Email dan password harus diisi")

        return data

    

class UserUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('nama','email','password')
    def update(self, instance, validated_data):
        instance.nama = validated_data('nama', instance.nama)
        instance.email = validated_data('email', instance.email)
        instance.password = validated_data('password', instance.password)
        instance.save()
        return instance

