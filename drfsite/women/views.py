from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, mixins  # , request
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets


class WomenAPIListPagination(PageNumberPagination):
    page_size = 3 # кол-во записей на страницу
    page_size_query_param = 'page_size' # кол-во записей на страницу, этим управляет клиент
    max_page_size = 10000


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (IsAuthenticated,) # разрешим получать доступ к отдельной записи
                                            # только авторизованным пользователям:
    authentication_classes = (TokenAuthentication,) #  данные по записи можно получать
                                                        # только при авторизации только по токенам
    pagination_class = WomenAPIListPagination


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)
