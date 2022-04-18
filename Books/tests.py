from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from BackendBestBooks.tests_dependencies import PathsBuilder


class TestStatusResponse(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.path_builder = PathsBuilder()
        self.path = self.path_builder.build_categories_url()

    def test_categories_response(self):
        print(self.path)
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


