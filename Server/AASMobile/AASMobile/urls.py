"""
URL configuration for AASMobile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myaap.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UserModelAPIView.as_view(), name='user-list'),
    path('api/games/', gamesModelAPIView.as_view(), name='game-list'),
    path('api/games/<int:pk>', gamesModelAPIView.as_view(), name='game-detail' ),
    path('api/auth/login/', UserLoginAPIView.as_view())
]
