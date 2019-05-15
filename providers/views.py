from django.contrib.gis.geos import Point
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from providers.models import Providers, ServiceAreas
from providers.serializers import ProvidersSerializer, ServiceAreaSerializer, SearchServiceAreaSerializer


class ProvidersViewSet(viewsets.ModelViewSet):
    """
        retrieve:
        Return the given provider.

        list:
        Return a list of all the existing providers.

        create:
        Create a new provider instance.
    """
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer


class ServiceAreasViewSet(viewsets.ModelViewSet):
    """
            retrieve:
            Return the given service area.

            list:
            Return a list of all the existing service areas.

            create:
            Create a new service area instance.
    """
    queryset = ServiceAreas.objects.all()
    serializer_class = ServiceAreaSerializer


class SearchView(APIView):
    '''
    param: coordinates: pair of coordinates example: -52.1026611328125,-5.752639602851877
    '''

    def get(self, request):
        coordinates = self.request.GET.get('coordinates')
        if not coordinates:
            raise ValidationError('You must pass the coordinate as a query string parameter')
        lat, long = tuple(coordinates.split(','))

        point = Point(float(lat), float(long))
        service_areas = ServiceAreas.objects.filter(service_area__intersects=point)
        serializer = SearchServiceAreaSerializer(service_areas, many=True)

        return JsonResponse(serializer.data)
