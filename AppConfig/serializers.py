from rest_framework import serializers

from AppConfig.models import Schema


class SchemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = '__all__'
