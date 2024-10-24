from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Kitten, Breed, User


class KittensTests(APITestCase):
    def setUp(self) -> None:
        test_user1 = User.objects.create_user(username='user_test1', email='sas@mail.ru', password='qwerty')
        test_user1.save()
        test_user2 = User.objects.create_user(username='test2', email='sas@mail.ru', password='qwerty2')
        test_user2.save()
        self.data_to_token = {"username": "test2",
                              "password": "qwerty2"}
        self.response_token = self.client.post(reverse('token_obtain_pair'), self.data_to_token, format="json")
        self.access_token = f'Bearer {self.response_token.data["access"]}'
        self.refresh_token = self.response_token.data["refresh"]

        self.kitten_data = {'age': '2222',
                            'color': 'RGB',
                            'breed': '1',
                            'title': 'ururu',
                            }

        Breed.objects.create(name='siam')
        Kitten.objects.create(age=1212, color='RedBlueWhite', breed_id=1, title='another', user=test_user2)
        Kitten.objects.create(age=2323, color='Babel', breed_id=1, title='treti', user=test_user1)

    def test_jwt_token(self):
        """Тест получения jwt токена"""
        print('test_jwt_token')

        self.assertEqual(self.response_token.status_code, status.HTTP_200_OK)

    def test_kitten_add(self):
        """Тест добавления записи о котенке"""
        print('test_add_kitten')
        url = reverse('add_kitten')
        response = self.client.post(url, self.kitten_data, format='json', headers={'Authorization': self.access_token})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual({'id': 3, 'age': 2222, 'color': 'RGB', 'breed': 1, 'title': 'ururu'}, response.data)
        self.assertEqual(Kitten.objects.get(id=3).user.username, 'test2')

    def test_fail_kitten_add(self):
        """Тест ошибки добавления записи о котенке"""
        print('test_fail_kitten_add')
        url = reverse('add_kitten')
        response = self.client.post(url, self.kitten_data, format='json')

        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Kitten.objects.count(), 2)

    def test_get_list_kittens(self):
        """тест получения списка котят"""
        print('test_get_list_kittens')
        url = reverse('get_list_kittens')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Kitten.objects.count(), 2)
        self.assertTrue({'id': 2, 'age': 2323, 'color': 'Babel', 'breed': 1, 'title': 'treti'} in response.data)

    def test_detail_kitten(self):
        """тест записи о котенке"""
        print('test_detail_kitten')
        url = reverse('detail_kittens', kwargs={'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'id': 1, 'age': 1212, 'color': 'RedBlueWhite', 'breed': 1, 'title': 'another'})

    def test_destroy_kitten(self):
        """Тест доступа к удалению записи"""
        print('test_destroy_kitten')
        url = reverse('detail_kittens', kwargs={'pk': 1})
        response = self.client.delete(url, headers={'Authorization': self.access_token})

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Kitten.objects.count(), 1)

    def test_fail_destroy_kitten(self):
        """Тест ошибки доступа к удалению записи"""
        print('test_destroy_kitten')
        url = reverse('detail_kittens', kwargs={'pk': 2})
        response = self.client.delete(url, headers={'Authorization': self.access_token})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Kitten.objects.count(), 2)
