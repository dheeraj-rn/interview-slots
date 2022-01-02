from rest_framework import serializers

from interview_apis.models import Users, Slots


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'user_type')


class SlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slots
        fields = ('user', 'available_from', 'available_to')
