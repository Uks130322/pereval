from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve, path, include
from rest_framework import status

from . import views
import json
from .models import PerevalAdded, User, Level, Coords, Image
from rest_framework.test import APITestCase
from .serializers import PerevalSerializer


class TestViews(TestCase):

    urlpatterns = [
        path('api/', include('pass_app.urls')),
    ]

    def test_pereval_list(self):
        client = Client()
        response = client.get(reverse('pereval-list'))
        self.assertEqual(response.status_code, 200)


class SubmitDataAPITests(APITestCase):
    urlpatterns = [
        path('api/', include('pass_app.urls')),
    ]

    def setUp(self):
        self.pereval1 = PerevalAdded.objects.create(
            user=User.objects.create(
                email='test@test.org',
                fam='test fam',
                name='test name',
                otc='test otc',
                phone='+1234567890'
            ),
            beauty_title='test beauty title',
            title='test title',
            other_titles='tests other titles',
            connect='test connect',
            status='new',
            coords=Coords.objects.create(
                latitude=12.123,
                longitude=34.345,
                height=1234,
            ),
            level=Level.objects.create(
                winter="",
                spring="",
                summer="1А",
                autumn="",
            )
        )
        self.image_list = [
            Image.objects.create(
                data='test data',
                title='test title',
                pereval=self.pereval1
            ),
            Image.objects.create(
                data='test data 2',
                title='test title 2',
                pereval=self.pereval1
            )
        ]

        self.pereval2 = PerevalAdded.objects.create(
            user=User.objects.create(
                email='test2@test.org',
                fam='test2 fam',
                name='test2 name',
                otc='test2 otc',
                phone='+1234567890'
            ),
            beauty_title='test beauty title 2',
            title='test title 2',
            other_titles='tests other titles 2',
            connect='test connect',
            status='new',
            coords=Coords.objects.create(
                latitude=13.123,
                longitude=35.345,
                height=1235,
            ),
            level=Level.objects.create(
                winter="",
                spring="1А",
                summer="",
                autumn="",
            )
        )
        self.image_list = [
            Image.objects.create(
                data='test data 2',
                title='test title 2',
                pereval=self.pereval1
            ),
        ]

    def test_create(self):
        response = self.client.post(reverse('pereval-list'), {
            "beauty_title": "test_beauty_title",
            "title": "test_title",
            "other_titles": "test_other_titles",
            "user": {"email": "test@test.org",
                     "fam": "test fam",
                     "name": "test name",
                     "otc": "test otc",
                     "phone": "+1234567890"},
            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"},
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": "1А"
            },
            "images": [
                {"data": "https://picture1.jpg",
                 "title": "test title"},
                {"data": "https://picture2.jpg",
                 "title": "test title 2"}]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list(self):
        response = self.client.get(reverse('pereval-list'))
        serializer_data = PerevalSerializer([self.pereval2, self.pereval1], many=True).data
        self.maxDiff = None
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PerevalAdded.objects.count(), 2)
        self.assertEqual(serializer_data, response.data)
        pereval_object1 = PerevalAdded.objects.filter(user__email='test@test.org').first()
        self.assertEqual(pereval_object1.beauty_title, 'test beauty title')
        pereval_object2 = PerevalAdded.objects.filter(user__email='test2@test.org').first()
        self.assertEqual(pereval_object2.beauty_title, 'test beauty title 2')

    def test_detail(self):
        response = self.client.get(reverse('pereval-detail',
                                           args={self.pereval1.pk}))
        serializer_data = PerevalSerializer(self.pereval1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_not_found(self):
        response = self.client.get(reverse('pereval-detail',
                                           args={500}))
        serializer_data = PerevalSerializer(self.pereval2).data
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_ok(self):
        response = self.client.put(reverse('pereval-detail',
                                           args={self.pereval1.pk}), {
            "beauty_title": "test_beauty_title",
            "title": "test_title",
            "other_titles": "test_other_titles_changed",  # changed
            "user": {"email": "test@test.org",
                     "fam": "test fam",
                     "name": "test name",
                     "otc": "test otc",
                     "phone": "+1234567890"},
            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"},
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": "1А"
            },
            "images": [
                {"data": "https://picture1.jpg",
                 "title": "test title"},
                {"data": "https://picture2.jpg",
                 "title": "test title 2"}]
        })
        self.assertEqual(response.json()['state'], 1)

    def test_update_bad_request_change_user(self):
        response = self.client.put(reverse('pereval-detail',
                                           args={self.pereval1.pk}), {
            "beauty_title": "test_beauty_title",
            "title": "test_title",
            "other_titles": "test_other_titles_changed",
            "user": {"email": "test2@test.org",  # changed
                     "fam": "test fam",
                     "name": "test name",
                     "otc": "test otc",
                     "phone": "+1234567890"},
            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"},
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": "1А"
            },
            "images": [
                {"data": "https://picture1.jpg",
                 "title": "test title"},
                {"data": "https://picture2.jpg",
                 "title": "test title 2"}]
        })
        self.assertEqual(response.json()['state'], 0)
        self.assertEqual(response.json()['message'], "Изменение данных пользователя невозможно")

    def test_update_bad_request(self):
        response = self.client.put(reverse('pereval-detail',
                                           args={self.pereval1.pk}), {
            "not_beauty_title": "test_beauty_title",
            "title": "test_title",
            "other_titles": "test_other_titles_changed",
            "user": {"email": "test@test.org",
                     "fam": "test fam",
                     "name": "test name",
                     "otc": "test otc",
                     "phone": "+1234567890"},
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": "1А"  # no images
            }})
        self.assertEqual(response.json()['state'], 0)

    def test_partial_update(self):
        response = self.client.patch(reverse('pereval-detail',
                                             args={self.pereval1.pk}), {
            "beauty_title": "test_beauty_title",
            "title": "test_title",
            "other_titles": "test_other_titles_changed",
            "user": {"email": "test2@test.org",
                     "fam": "test fam",
                     "name": "test name",
                     "otc": "test otc"},
            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"},
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": "1А"
            }})
        self.assertEqual(response.json()['state'], 0)
