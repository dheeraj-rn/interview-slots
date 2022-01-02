from django.urls import include, path

from rest_framework import routers

from interview_apis.views import UserViewSet, SlotsViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'slots', SlotsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
