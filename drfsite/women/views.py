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



# class WomenAPIView(APIView):
#
#     def get(self, request):
#         w = Women.objects.all() # список статей получаем как набор queryset
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data) # проверка, если данные в БД отсутствуют
#         serializer.is_valid(raise_exception=True)
#         serializer.save() # этот метод save() автоматически вызовет метод create из serializers.py
#
#         return Response({'post': serializer.data}) # serializer.data - коллекция которую возвратит метод create
#         # serializer.data - мы не создаем новый словарь, а воспользуемся уже созданныым на строке 22
#         # return Response({'post': WomenSerializer(post_new).data})
#
#
#
#     def put(self, request, *args, **kwargs): # что положим (изменим)
#         pk = kwargs.get('pk', None)
#             # pk - идентификатор записи, которую нужно поменять
#             # обращаемся к словарю kwargs, берем (.get) из него ключ pk
#             # а если ключ там не присутствует, возвращаем None
#         if not pk: # если ключ там не присутствует, то
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#                 # извлекаем запись из модели Women по ключу pk
#         except: # иначе:
#             return Response({"error": "Object does not exists"})
#
#             # и когда мы получили и ключ и запись по этому ключу, то создаем сериализатор
#         serializer = WomenSerializer(data=request.data, instance=instance)
#             # request.data - те данные которые нам нужно изменить
#             # instance - объект, - та запись, которую мы собираемся поменять
#         serializer.is_valid(raise_exception=True)
#         serializer.save() # здесь метод save автоматически вызовет метод update из serializer.py
#             # после того как поменяли запись, отправляем клиенту запись в виде JSON-строки
#         return Response({"post": serializer.data}) # serializer.data - те данные,которые были изменены
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)  # получили ключ
#         if not pk: # а если его нет,то:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#                 # извлекаем запись из модели Women по ключу pk
#         except: # иначе:
#             return Response({"error": "Object does not exists"})
#
#             # и когда мы получили и ключ и запись по этому ключу, то создаем сериализатор
#         serializer = WomenSerializer(data=request.data, instance=instance)
#             # request.data - те данные которые нам нужно изменить
#             # instance - объект, - та запись, которую мы собираемся поменять
#         serializer.is_valid(raise_exception=True)
#         instance.delete()
#         # после того как поменяли запись, отправляем клиенту запись в виде JSON-строки
#         return Response({"post": "delete post " + str(pk)}) # и возвратить этот ответ клиенту
