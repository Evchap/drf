from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, mixins  # , request
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets

# задаем 3 класса обычных представлений
class WomenAPIList(generics.ListCreateAPIView): # класс отдает список записей из таблицы women и позволяет создать новую запись
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)

class WomenAPIUpdate(generics.RetrieveUpdateAPIView): #  – меняет выбранную запись только автор,
                                                    # а просматривать могут все пользователи
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,) # сделаем так, чтобы добавлять записи могли только
                                                        # авторизованные пользователи.


class WomenAPIDestroy(generics.RetrieveDestroyAPIView): # – удаляет выбранную запись
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,) # если, предположим, удалять может только администратор
