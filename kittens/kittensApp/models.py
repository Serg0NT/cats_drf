from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Breed(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name='Порода')

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return f'{self.name}'


#
# class Owner(models.Model):
#     name = models.CharField(max_length=24, blank=True, null=True, verbose_name='Имя')
#     surname = models.CharField(max_length=24, blank=True, null=True, verbose_name='Фамилия')
#     age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(18)], verbose_name='Возраст')
#
#     def __str__(self):
#         return f'{self.name} {self.surname}'


class Kitten(models.Model):
    age = models.IntegerField(default=1, blank=False, null=False, verbose_name='Возраст')
    color = models.CharField(max_length=40, blank=False, null=False, verbose_name='Цвет')
    breed = models.ForeignKey(Breed, null=True, blank=True,
                              related_name='kittens',
                              on_delete=models.SET_NULL,
                              verbose_name='Порода')
    title = models.TextField(max_length=256, verbose_name='Описание')
    user = models.ForeignKey(User, null=True, blank=True,
                             related_name='owners',
                             on_delete=models.CASCADE,
                             verbose_name='Хозяин')

    def __str__(self):
        return f'{self.breed} {self.color} {self.age}'
