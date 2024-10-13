from django.urls import path
from .views import (KittensApiList,
                    KittensApiAdd,
                    BreedsApiList,
                    BreedsRetrieveUpdateDestroy,
                    KittensRetrieveUpdateDestroy,
                    KittensOfBreedApi
                    )

urlpatterns = [
    # Просмотр всех котят
    path('kittens/', KittensApiList.as_view()),
    # Добавление нового котенка
    path('kittens/add/', KittensApiAdd.as_view()),
    # Просмотр, добавление информации или удаление котенка по id
    path('kittens/<int:pk>/', KittensRetrieveUpdateDestroy.as_view()),
    # Просмотр всех пород
    path('breeds/', BreedsApiList.as_view()),
    # Просмотр, добавление информации или удаление породы по id
    path('breeds/<int:pk>/', BreedsRetrieveUpdateDestroy.as_view()),
    # Просмотр всех котят определенной породы
    path('breeds/kittens/<int:pk>/', KittensOfBreedApi.as_view()),
]
