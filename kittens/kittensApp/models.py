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


class Kitten(models.Model):
    age = models.IntegerField(default=1, blank=False, null=False, verbose_name='Возраст')
    color = models.CharField(max_length=40, blank=False, null=False, verbose_name='Цвет')
    breed = models.ForeignKey(Breed, null=True, blank=True,
                              related_name='kittens',
                              on_delete=models.SET_NULL,
                              verbose_name='Порода')
    title = models.TextField(max_length=256, verbose_name='Описание')
    user = models.ForeignKey(User, null=True, blank=True,
                             related_name='kittens',
                             on_delete=models.CASCADE,
                             verbose_name='Хозяин')

    class Meta:
        verbose_name = 'Котята'
        verbose_name_plural = 'Котят'

    def __str__(self):
        return f'Порода - {self.breed}, ' \
               f'Цвет -  {self.color}, ' \
               f'Возраст -  {self.age}, ' \
               f'Хозяин -  {self.user}'
