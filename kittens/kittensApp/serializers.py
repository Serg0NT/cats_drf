from rest_framework import serializers
from .models import Kitten, Breed


class KittenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # breed = serializers.PrimaryKeyRelatedField(queryset=Kitten.objects.all())

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
    kittens = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Breed
        fields = ['name',
                  'kittens']


class ShowKittensOfBreedSerializer(serializers.ModelSerializer):
    kittens = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Breed
        fields = ['kittens']
