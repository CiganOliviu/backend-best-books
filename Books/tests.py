from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from BackendBestBooks.tests_dependencies import PathsBuilder


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
    pass
