from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly

from .serializers import KittenSerializer, BreedSerializer, UserSerializer
from .models import Kitten, Breed, User


# Просмотр всех котят
class KittensApiList(generics.ListAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer


# Просмотр, добавление информации или удаление котенка по id
class KittensRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsOwnerOrReadOnly]


#  Добавление нового котенка
class KittensApiAdd(generics.CreateAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated]


class BreedsApiList(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittensFilterUser(generics.ListAPIView):
    serializer_class = KittenSerializer

    def get_queryset(self):
        return Kitten.objects.filter(user_id=self.kwargs['user_id'])


class KittensFilterBreed(generics.ListAPIView):
    serializer_class = KittenSerializer

    def get_queryset(self):
        return Kitten.objects.filter(breed_id=self.kwargs['breed_id'])


# Просмотр, добавление информации или удаление породы по id
# class BreedsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Breed.objects.all()
#     serializer_class = BreedSerializer
#     permission_classes = [IsAdminOrReadOnly]
