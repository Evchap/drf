from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all() # список статей получаем как набор queryset
        return Response({'posts': WomenSerializer(w, many=True).data})
        # и с помощью сериализатора WomenSerializer. many=True - сериализатор обрабатывает список записей
        # data - словарь преобразованных данных из таблицы Women

    def post(self, request):
        serializer = WomenSerializer(data=request.data) # проверка, если данные в БД отсутствуют
        serializer.is_valid(raise_exception=True)
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': WomenSerializer(post_new).data})


# class WomenAPIView(APIView):
#     def get(self, request): # простейший get-запрос без сериализатора
#         lst = Women.objects.all().values()
#         return Response({'posts': list(lst)})
#
#     def post(self, request):
#         post_new = Women.objects.create( # objects - это менеджер
#             title=request.data['title'], #title берет из коллекции request значение data по ключу (поле) ['title']
#             content=request.data['content'], #
#             cat_id=request.data['cat_id'] #
#         )
#         return Response({'post': model_to_dict(post_new)}) # получить значения, что именно добавили в БД
#                         # ключ 'post', а значение - функция model_to_dict, который преобразовывает объект класса Women
#                         # из модели Джанго в словарь

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

