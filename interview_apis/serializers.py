from rest_framework import serializers
from rest_framework.views import set_rollback

from interview_apis.models import Users, Slots


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'user_type')


class SlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slots
        fields = ('user', 'available_from', 'available_to')


class UserSlotsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_user_name')
    user_id = serializers.SerializerMethodField('get_user_id')
    user_type = serializers.SerializerMethodField('get_user_type')

    class Meta:
        model = Slots
        fields = ('user_id', 'name', 'user_type',
                  'available_from', 'available_to')

    def get_user_name(self, obj):
        return obj.user.name

    def get_user_id(self, obj):
        return obj.user.id

    def get_user_type(self, obj):
        return obj.user.user_type
