
from django.contrib import admin
from django.urls import path, include, re_path

from women.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')), # Авторизация на основе сессии и cookies
        # 'api/v1/drf-auth/' этот маршрут мы придумываем сами
        #  из rest_framework подключаем эти маршруты .urls
    path('api/v1/women/', WomenAPIList.as_view()), # для получения списка статей
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()), # для изменения записи
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()), # для удаления записи
    path('api/v1/auth/', include('djoser.urls')),  # new # подключают Djoiser (аутентификация по токенам) к проекту
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new # подключают Djoser (аутентификация по токенам) к проекту
]