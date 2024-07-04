from rest_framework import serializers
from .models import Pengguna, detailPengguna


class penggunaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = '__all__'

class detailPenggunaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = detailPengguna
        fields = '__all__'


