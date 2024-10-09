from rest_framework import mixins, generics, status
from rest_framework.permissions import IsAdminUser
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly

from .serializers import KittenSerializer, BreedSerializer
from .models import Kitten, Breed


# Просмотр всех котят
class KittensApiList(generics.ListAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    # permission_classes = [IsAuthenticated]


# Просмотр, добавление информации или удаление котенка по id
class KittensRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsOwnerOrReadOnly]


#  Добавление нового котенка
class KittensApiAdd(generics.CreateAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer


class BreedsApiList(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


# Просмотр, добавление информации или удаление породы по id
class BreedsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAdminOrReadOnly]

