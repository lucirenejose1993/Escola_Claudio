"""Escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('disciplina/', disciplina),
    path('disciplina_1/', disciplina_1),
    path('listacurso/', lista_curso),
    path('noticias/', noticias),
    path('det_1', detalhe_1),
    path('det_2', detalhe_2),
    path('det_3', detalhe_3),
    path('det_4', detalhe_4),
    path('bg', big_data),
    path('dw', data_w),
    path('ct', comp_th),
    path('da', data_a),
    path('ad', admin_rede),
    path('cv', conv_dig),
    path('ec', cenario),
    path('mk', marketing),

]

