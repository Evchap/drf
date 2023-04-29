import io
from rest_framework import serializers
from .models import Women


# У нас появилась форма для добавления записи, т.к. мы теперь воспринимаемся системой как авторизованные
# пользователи. Правда, у этой формы есть один недостаток. Добавляя запись, мы можем указать любого пользователя,
# который как будто добавил ее. Правильнее было бы это поле формировать автоматически,
# записывая в него данные текущего пользователя.
class WomenSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Women
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
        # HiddenField - скрытое поле, и в нем:
        # по умолчанию default прописывается текущий пользователь
        fields = "__all__"

