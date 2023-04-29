
from django.contrib import admin
from django.urls import path, include

from women.views import *
from rest_framework import routers

# создаем роутер
router = routers.SimpleRouter() # из ветки routers мы обратимся к классу SimpleRouter()
# связываем этот роутер с вьюсетом WomenViewSet.
# Делается это с помощью метода register
router.register(r'women', WomenViewSet)
    # регистрируем метод вьюсЕта - router.register
    # r - префикс для набора маршрутов
    # WomenViewSet - класс вьюсета

# до роутера
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
#     # для метода 'get прописываем дополнительно словарь list
#     # В частности, метод as_view({'get': 'list'}) связывает GET-запрос с возвратом клиенту списка записей из модели таблицы БД.
#     # А метод as_view({'put': 'update'}) связывает PUT-запрос с методом update() для изменения текущей записи.
#     path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
# ]

# с роутером
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),   # http://127.0.0.1:8000/api/v1/women/
    # коллекция маршрутов urlpatterns, которые создал роутер
    # include - включая
    # когда мы зарегистрировали роутер стр. 12, то в роутере автомматически генерируется коллекция (router.urls)
    # как формируется маршрут:
    # стр. 30 сначала 'api/v1/', потом (смотреть в конце строки 30) - /women/
]