from django.urls import path
from .views_api import (KittensApiList,
                        KittensApiAdd,
                        BreedsApiList,
                        # BreedsRetrieveUpdateDestroy,
                        KittensRetrieveUpdateDestroy, KittensFilterUser, KittensFilterBreed,
                        )

urlpatterns = [
    # Просмотр всех котят
    path('kittens/', KittensApiList.as_view(), name='get_list'),
    # Добавление нового котенка
    path('kittens/add/', KittensApiAdd.as_view(), name='add_kitten'),
    # Просмотр, добавление информации или удаление котенка по id
    path('kittens/<int:pk>/', KittensRetrieveUpdateDestroy.as_view(), name='detail_kittens'),
    # Просмотр всех котят определенного юзера по id
    path('kittens/user/<int:user_id>/', KittensFilterUser.as_view(), name='kittens_filter_user'),
    # Просмотр всех пород
    path('breeds/', BreedsApiList.as_view()),
    # Просмотр всех котят определенной породы
    path('breeds/<int:breed_id>/', KittensFilterBreed.as_view(), name='kittens_filter_breed'),
    # Просмотр, добавление информации или удаление породы по id
    # path('breeds/<int:pk>/', BreedsRetrieveUpdateDestroy.as_view()),

]
