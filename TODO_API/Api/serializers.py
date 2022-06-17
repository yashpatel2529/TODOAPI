from Api.models import Todo
from Api.models import Register
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Todo
        fields ="__all__"
        # fields = (
        #     'id',
        #     'title',
        #     'description',
        # )


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"


