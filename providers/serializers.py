from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from providers.models import Providers, ServiceAreas


class ProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providers
        fields = '__all__'


class SearchProvidersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Providers
        fields = ('name',)


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ServiceAreas
        fields = '__all__'
        geo_field = 'service_area'


class SearchServiceAreaSerializer(GeoFeatureModelSerializer):
    provider = SearchProvidersSerializer()

    class Meta:
        model = ServiceAreas
        fields = '__all__'
        geo_field = 'service_area'
