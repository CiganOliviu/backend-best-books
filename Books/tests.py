from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from rest_framework.utils import json

from BackendBestBooks.tests_dependencies import PathsBuilder
from Books.models import Nationalitie, Categorie, Author, Book


class TestStatusResponse(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.path_builder = PathsBuilder()

    def test_categories_response(self):
        path = self.path_builder.build_categories_url()
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_nationalities_response(self):
        path = self.path_builder.build_nationalities_url()
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authors_response(self):
        path = self.path_builder.build_authors_url()
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_books_response(self):
        path = self.path_builder.build_books_url()
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestDataResponse(APITestCase):
    def setUp(self):
        self.path_builder = PathsBuilder()

        Nationalitie.objects.create(
            name='American'
        )

        Categorie.objects.create(
            name='Business'
        )

        Author.objects.create(
            profile='authors-profile-images/default.jpg',
            first_name='Bob',
            last_name='Martin',
            age='69',
            nationality=Nationalitie.objects.get(id=1),
            occupation='Software Engineer',
            website='www.cleancoder.com'
        )

        Book.objects.create(
            title='Clean Code',
            description='Simple description',
            mark=10,
            cover='books-cover-images/default.jpg',
            current_market_price='300',
            pages='456',
            category=Categorie.objects.get(id=1),
            virtually_owned=True,
            physically_owned=False
        )

        authors = Author.objects.all()
        book = Book.objects.get(id=1)
        book.authors.add(*authors)

    def test_nationalities_response_data(self):
        expected_json_response = {
            'id': 1,
            'name': 'American'
        }

        response = self.client.get(self.path_builder.build_nationalities_url(), format='json',
                                   content_type='application/json')
        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(expected_json_response, sort_keys=True)
        self.assertEqual(response_data_as_json, expected_response_data_as_json)

    def test_categories_response_data(self):
        expected_json_response = {
            'id': 1,
            'name': 'Business'
        }

        response = self.client.get(self.path_builder.build_categories_url(), format='json',
                                   content_type='application/json')
        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(expected_json_response, sort_keys=True)
        self.assertEqual(response_data_as_json, expected_response_data_as_json)

    def test_authors_response_data(self):
        expected_json_response = {
            'id': 1,
            'profile': '/MEDIA/authors-profile-images/default.jpg',
            'first_name': 'Bob',
            'last_name': 'Martin',
            'age': '69',
            'nationality': {
                'id': 1,
                'name': 'American'
            },
            'occupation': 'Software Engineer',
            'website': 'www.cleancoder.com'
        }

        response = self.client.get(self.path_builder.build_authors_url(), format='json',
                                   content_type='application/json')
        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(expected_json_response, sort_keys=True)
        self.assertEqual(response_data_as_json, expected_response_data_as_json)

    def test_books_response_data(self):
        expected_json_response = {
            'id': 1,
            'authors': [{
                    'id': 1,
                    'profile': '/MEDIA/authors-profile-images/default.jpg',
                    'first_name': 'Bob',
                    'last_name': 'Martin',
                    'age': '69',
                    'nationality': {
                        'id': 1,
                        'name': 'American'
                    },
                    'occupation': 'Software Engineer',
                    'website': 'www.cleancoder.com'
            }],
            'title': 'Clean Code',
            'description': 'Simple description',
            'mark': '10',
            'cover': '/MEDIA/books-cover-images/default.jpg',
            'current_market_price': '300',
            'pages': '456',
            'category': {
                'id': 1,
                'name': 'Business',
            },
            'virtually_owned': True,
            'physically_owned': False
        }

        response = self.client.get(self.path_builder.build_books_url(), format='json',
                                   content_type='application/json')
        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(expected_json_response, sort_keys=True)
        self.assertEqual(response_data_as_json, expected_response_data_as_json)
