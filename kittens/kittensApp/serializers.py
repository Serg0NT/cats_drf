from rest_framework import serializers
from .models import Kitten, Breed


class KittenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Kitten
        fields = [
            'id',
            'age',
            'color',
            'breed',
            'title',
            'user',
        ]


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = [
            'name',
        ]
