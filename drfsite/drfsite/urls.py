
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import MyCustomRouter

from women.views import *
from rest_framework import routers

# class MyCustomRouter(routers.SimpleRouter): # создание собственного класса роутера (взят из документации)
#     routes = [ # routes - список из маршрутов
#         # routers.Route 1-ый маршрут - определяет список статей
#         routers.Route(url=r'^{prefix}$', # ^{prefix}$ - регулярное выражение
                                            # надо запомнить, что адреса здесь определены без обратного слеша
#                       mapping={'get': 'list'}, # связывает тип запроса с соответствующим методом ViewSet
#                       name='{basename}-list',
#                       detail=False, # список или отдельная запись
#                       initkwargs={'suffix': 'List'}), # при срабатывании маршрута передает аргументы
#         # дополнительные аргументы для коллекции kwargs, которые передаются конкретному представлению при срабатывании маршрута.
#
#         # routers.Route - 2-ой маршрут - определяет конкретную статью по ее идентификатору
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]


# router = routers.DefaultRouter()
# # router.register(r'women', WomenViewSet)
# router.register(r'women', WomenViewSet, basename='women') # Но, так как мы используем роутер ,
#                                                         # то нужно прописать параметр basename:
# print(router.urls)

router = MyCustomRouter()
# router.register(r'women', WomenViewSet)
router.register(r'women', WomenViewSet, basename='women')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),   # http://127.0.0.1:8000/api/v1/women/

]