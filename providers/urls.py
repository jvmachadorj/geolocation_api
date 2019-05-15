from django.urls import path
from rest_framework import routers

from providers.views import ProvidersViewSet, ServiceAreasViewSet, SearchView

router = routers.SimpleRouter()
router.register(r'providers', ProvidersViewSet, basename='providers')
router.register(r'service_areas', ServiceAreasViewSet, basename='service_areas')

urlpatterns = [
    path('search', SearchView.as_view())
]

urlpatterns += router.urls
