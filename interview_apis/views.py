from rest_framework import viewsets

from interview_apis.serializers import UsersSerializer, SlotsSerializer
from interview_apis.models import Users, Slots


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class SlotsViewSet(viewsets.ModelViewSet):
    queryset = Slots.objects.all()
    serializer_class = SlotsSerializer
