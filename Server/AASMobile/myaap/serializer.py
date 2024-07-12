import base64
from rest_framework import serializers
from .models import Users, Games, detail_user, userManager
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    nama = serializers.CharField(required=True)
    def validate(self, attrs):
        credentials = {
            'nama': attrs.get('nama'),
            'password': attrs.get('password')
        }
        if all(credentials.values()):
            user_query = Users.objects.filter(nama=credentials['nama'])
            if not user_query.exists():
                raise serializers.ValidationError('User tidak ditemukan')
            user = user_query.first()
            if not user.check_password(credentials['password']):
                raise serializers.ValidationError('Password salah')
            refresh = self.get_token(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'nama': user.nama,
                'email': user.email,
                'created_at': user.created_at
            }
        else:
            raise serializers.ValidationError('Tidak ada kredensial yang diberikan')

    def get_token(self, user):
        token = super().get_token(user)
        return token
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
class GamesModelSerializer(serializers.ModelSerializer):
    # gambar_game_base64 = serializers.SerializerMethodField()
    class Meta:
        model = Games
        fields = '__all__'
        
class detailUsersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = detail_user
        fields = 'user_id'

class UserRegistrasiModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ['nama','email','password']
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            hashed_password = make_password(password)
            instance.password = hashed_password
        instance.save()
        return instance

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = Users.objects.get(email=email, password=password)
                # jika user ditemukan, return validated data
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


