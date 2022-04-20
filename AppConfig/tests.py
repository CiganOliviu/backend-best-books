from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from rest_framework.utils import json

from AppConfig.models import Schema
from BackendBestBooks.tests_dependencies import PathsBuilder


class TestStatusResponse(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.path_builder = PathsBuilder()

    def test_schemas_response(self):
        path = self.path_builder.build_schemas_url()
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestDataResponse(APITestCase):
    def setUp(self):
        self.path_builder = PathsBuilder()

        Schema.objects.create(
            route='/index',
            name='index'
        )

    def test_schemas_response_data(self):
        expected_json_response = {
            'id': 1,
            'route': '/index',
            'name': 'index'
        }

        response = self.client.get(self.path_builder.build_schemas_url(), format='json',
                                   content_type='application/json')
        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(expected_json_response, sort_keys=True)
        self.assertEqual(response_data_as_json, expected_response_data_as_json)
