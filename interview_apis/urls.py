from django.urls import include, path

from rest_framework import routers

from interview_apis.views import UserViewSet, SlotsViewSet, CustomUserSlotView

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'slots', SlotsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'available_slot', CustomUserSlotView.as_view()),
]
