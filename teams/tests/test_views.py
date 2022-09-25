from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from teams.tests.factories import PokemonFactory, TeamFactory, TrainerFactory
from teams.models import Team, Trainer

# Trainer Test Views
class TrainerViewSetTestCase(TestCase):

    def setUp(self):
        self.data = {'name': 'Test'}
        self.client = Client()

    def test_get_list(self):

        trainers = [TrainerFactory() for i in range(0, 3)]
        list_url = reverse('api:trainer-list')
        response = self.client.get(list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(trainer.get('id') for trainer in response.data.get('results')),
            set(trainer.id for trainer in trainers)
        )

    def test_get_detail(self):

        trainer = TrainerFactory()
        detail_url = reverse('api:trainer-detail', kwargs={'pk': trainer.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), trainer.name)

    def test_post(self):

        self.assertEqual(Trainer.objects.count(), 0)

        create_url = reverse('api:trainer-list')
        response = self.client.post(create_url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trainer.objects.count(), 1)
        trainer = Trainer.objects.all().last()

        for field_name in self.data.keys():
            self.assertEqual(getattr(trainer, field_name), self.data.get(field_name))

    def test_put(self):

        trainer = TrainerFactory()

        put_url = reverse('api:trainer-detail', kwargs={'pk': trainer.id})
        response = self.client.put(put_url, data=self.data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # The object has really been updated
        trainer.refresh_from_db()
        for field_name in self.data.keys():
            self.assertEqual(getattr(trainer, field_name), self.data.get(field_name))

    def test_delete(self):

        trainer = TrainerFactory()
        delete_url = reverse('api:trainer-detail', kwargs={'pk': trainer.id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # 400 Bad Request
    def test_not_acceptable(self):

        trainer = TrainerFactory()

        with self.subTest('POST'):

            self.data['name'] = list()  # Bad data
            create_url = reverse('api:trainer-list')
            response = self.client.post(create_url, data=self.data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        with self.subTest('PUT'):

            self.data['name'] = list()  # Bad data

            put_url = reverse('api:trainer-detail', kwargs={'pk': trainer.id})
            response = self.client.put(put_url, data=self.data, content_type='application/json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

            # The object was not updated
            trainer.refresh_from_db()
            self.assertNotEqual(trainer.name, self.data.get('name'))

    # 404 Not found
    def test_not_found(self):

        with self.subTest('GET Detail'):

            detail_url = reverse('api:trainer-detail', kwargs={'pk': 0})  # Fake PK
            response = self.client.get(detail_url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        with self.subTest('PUT'):

            put_url = reverse('api:trainer-detail', kwargs={'pk': 0})  # Fake PK
            response = self.client.put(put_url, data=self.data, content_type='application/json')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        with self.subTest('DELETE'):

            delete_url = reverse('api:trainer-detail', kwargs={'pk': 0})  # Fake PK
            response = self.client.delete(delete_url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# Team Test Views
class TeamViewSetTestCase(TestCase):

    def setUp(self):
        self.data = {'trainer':TrainerFactory().pk, 'name': 'Test', 'pokemons': []}
        self.client = Client()

    def test_get_list(self):

        teams = [TeamFactory() for i in range(0, 3)]
        list_url = reverse('api:team-list')
        response = self.client.get(list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(team.get('id') for team in response.data.get('results')),
            set(team.id for team in teams)
        )

    def test_get_detail(self):

        team = TeamFactory()
        detail_url = reverse('api:team-detail', kwargs={'pk': team.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), team.name)

    def test_post(self):

        self.assertEqual(Team.objects.count(), 0)

        create_url = reverse('api:team-list')
        response = self.client.post(create_url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        team = Team.objects.all().last()

        for field_name in self.data.keys():
            if field_name in ['trainer']:
                self.assertEqual(getattr(team, field_name).pk, self.data.get(field_name))
            elif field_name in ['name']:
                self.assertEqual(getattr(team, field_name), self.data.get(field_name))

    def test_put(self):

        team = TeamFactory()

        put_url = reverse('api:team-detail', kwargs={'pk': team.id})
        response = self.client.put(put_url, data=self.data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # The object has really been updated
        team.refresh_from_db()
        for field_name in self.data.keys():
            if field_name in ['trainer']:
                self.assertEqual(getattr(team, field_name).pk, self.data.get(field_name))
            elif field_name in ['name']:
                self.assertEqual(getattr(team, field_name), self.data.get(field_name))

    def test_delete(self):

        team = TeamFactory()
        delete_url = reverse('api:team-detail', kwargs={'pk': team.id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # 400 Bad Request
    def test_not_acceptable(self):

        team = TeamFactory()

        with self.subTest('POST'):

            self.data['name'] = list()  # Bad data
            create_url = reverse('api:team-list')
            response = self.client.post(create_url, data=self.data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        with self.subTest('PUT'):

            self.data['name'] = list()  # Bad data

            put_url = reverse('api:team-detail', kwargs={'pk': team.id})
            response = self.client.put(put_url, data=self.data, content_type='application/json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

            # The object was not updated
            team.refresh_from_db()
            self.assertNotEqual(team.name, self.data.get('name'))

    # 404 Not found
    def test_not_found(self):

        with self.subTest('GET Detail'):

            detail_url = reverse('api:team-detail', kwargs={'pk': 0})  # Fake PK
            response = self.client.get(detail_url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        with self.subTest('PUT'):

            put_url = reverse('api:team-detail', kwargs={'pk': 0})  # Fake PK
            response = self.client.put(put_url, data=self.data, content_type='application/json')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        with self.subTest('DELETE'):

            delete_url = reverse('api:team-detail', kwargs={'pk': 0})  # Fake PK
            response = self.client.delete(delete_url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# Pokemon Test Views
class PokemonViewSetTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_list(self):

        list_url = reverse('api:pokemon-list')
        response = self.client.get(list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
