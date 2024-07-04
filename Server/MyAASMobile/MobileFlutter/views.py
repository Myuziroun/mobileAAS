from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pengguna, detailPengguna
from .serializers import penggunaModelSerializer, detailPenggunaModelSerializer


class penggunaModelAPIView(APIView):
    def get(self, request):
        pengguna = Pengguna.objects.all()
        serializer = penggunaModelSerializer(pengguna, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        
        serializer = penggunaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

