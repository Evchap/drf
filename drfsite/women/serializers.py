import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Women

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255) # Field - это валидаторы сериализаторов
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField() #
        # отличие - в models.py в class Momen cat_id определен как ForeignKey, то
        # в сериализаторе прописываем cat_id конкретным образом


    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
            # instance это ссылка на объект модели Women
            # validated_data это словарь из проверенных данных который нужно изменить
        instance.title = validated_data.get("title", instance.title)
            # "title" - ключ из словаря, а если этого ключа нет, то:
            # instance.title - возвращаем ключ из словаря модели Women
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance # возвращаем объект instance
