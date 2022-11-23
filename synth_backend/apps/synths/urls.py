from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import SynthViewSet

router = DefaultRouter()
router.register(f'synths', SynthViewSet, basename = 'synths')

urlpatterns = [
    path('', include(router.urls))
]