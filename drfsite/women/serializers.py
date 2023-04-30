import io
from rest_framework import serializers
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Women
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
        fields = "__all__"

