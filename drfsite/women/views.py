from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, mixins  # , request
from rest_framework.decorators import api_view, action

from .models import Women, Category
from .serializers import WomenSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets


# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer



# # с декоратором @action
# class WomenViewSet(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    viewsets.GenericViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     # @action(methods=['get'], detail=False)
#     # def category(self, request):
#     #     cats = Category.objects.all()
#     #     return Response({'cats': [c.name for c in cats]})
#
#
#     # допустим, нам нужно выводить список категорий. добавляем декоратор @action
#     @action(methods=['get'], detail=True) # methods - поддерживаемые методы
#     # detail=False - список категорий
#     # detail=True - только одна запись
#     # def category(self, request): # метод придумываем сами
#     def category(self, request, pk=None): # если появляется параметр pk,
#                                             # то мы выдает список из одной конкретной записи, пример:
#                                             # http://127.0.0.1:8000/api/vcats.name1/women/1/category/
#                                             # НАВЕСТИ КУРСОР НА АДРЕС НА СТРОКЕ ВЫШЕ И CTRL+v -
#                                             # откроется новое окно в браузере # n
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name}) # возвращаем в JSON формате
#                                             # cats.name - название категории


                                        #  Метод get_queryset
# ------------------- КОГДА НУЖНО ВОЗВРАЩАТЬ НЕ ВСЕ ЗАПИСИ, А ТОЛЬКО НУЖНЫЕ ---------------------

class WomenViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    #  queryset = Women.objects.all() # чтобы вывести первые 3 записи, а если мы применяем функцию get_queryset,
                                    # строку queryset = Women.objects.all() убрать
    serializer_class = WomenSerializer

    # def get_queryset(self): # возвращать список (у нас это список статей из БД)
    #     return Women.objects.all()[:3]


    def get_queryset(self): # возвращать только одну запись
        pk = self.kwargs.get("pk") # kwargs - локальная коллекция ключей
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)# если появляется параметр pk, то мы выдает список из одной конкретной записи,
                                            # а иначе – список из первых трех


    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
