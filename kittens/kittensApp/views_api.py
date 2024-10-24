from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly

from .serializers import KittenSerializer, BreedSerializer, UserSerializer
from .models import Kitten, Breed, User


# Просмотр всех котят
class KittensApiList(generics.ListAPIView):
    """Список всех котят"""
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer


# Просмотр, добавление информации или удаление котенка по id
class KittensRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение, удаление записи о котенке"""
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsOwnerOrReadOnly]


#  Добавление нового котенка
class KittensApiAdd(generics.CreateAPIView):
    """Добавление нового котенка"""
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated]


class KittensFilterUser(generics.ListAPIView):
    """Список котят определенного пользователя"""
    serializer_class = KittenSerializer

    def get_queryset(self):
        return Kitten.objects.filter(user_id=self.kwargs['user_id'])


class BreedsApiList(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittensFilterBreed(generics.ListAPIView):
    serializer_class = KittenSerializer

    def get_queryset(self):
        return Kitten.objects.filter(breed_id=self.kwargs['breed_id'])
