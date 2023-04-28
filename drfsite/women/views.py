from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics # , request
from rest_framework.decorators import api_view

from .models import Women
from .serializers import WomenSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class WomenAPIList(generics. ListCreateAPIView):
    queryset = Women.objects.all() # get запрос - получить список
    serializer_class = WomenSerializer # post - добавлять новую запись


class WomenAPIUpdate(generics.UpdateAPIView): # put запрос - изменить список
    queryset = Women.objects.all() # здесь клиенту будет отправлена только одна измененная запись
                                    # а не весь список, т.к. это ленивый запрос
    serializer_class = WomenSerializer

class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    # делает все: get, put, patch, delete
    queryset = Women.objects.all()
    serializer_class = WomenSerializer