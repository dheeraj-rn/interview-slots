from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from interview_apis.serializers import UsersSerializer, SlotsSerializer, UserSlotsSerializer
from interview_apis.models import Users, Slots
from datetime import datetime
from dateutil import parser


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class SlotsViewSet(viewsets.ModelViewSet):
    queryset = Slots.objects.all()
    serializer_class = SlotsSerializer


class CustomUserSlotView(APIView):

    def get(self, request, format=None):
        candidate_user_id = request.query_params.get('candidate_user_id')
        interviewer_user_id = request.query_params.get('interviewer_user_id')
        if not candidate_user_id or not interviewer_user_id:
            return Response(status=400, data={'message': 'candidate_user_id and interviewer_user_id are required'})
        candidate_user_slots = Slots.objects.filter(
            user_id=candidate_user_id)
        interviewer_user_slots = Slots.objects.filter(
            user_id=interviewer_user_id)
        candidate_user_slots_serializer = UserSlotsSerializer(
            candidate_user_slots, many=True)
        interviewer_user_slots_serializer = UserSlotsSerializer(
            interviewer_user_slots, many=True)
        candidate_aval_from = candidate_user_slots[0].available_from.strftime(
            '%Y-%m-%dT%H:%M:%S')
        candidate_aval_to = candidate_user_slots[0].available_to.strftime(
            '%Y-%m-%dT%H:%M:%S')
        interviewer_aval_from = interviewer_user_slots[0].available_from.strftime(
            '%Y-%m-%dT%H:%M:%S')
        interviewer_aval_to = interviewer_user_slots[0].available_to.strftime(
            '%Y-%m-%dT%H:%M:%S')
        overlap = candidate_aval_from <= interviewer_aval_to and interviewer_aval_from <= candidate_aval_to
        if not overlap:
            return Response(status=400, data={'message': 'No overlap'})
        lower_bound = max(candidate_aval_from, interviewer_aval_from)
        upper_bound = min(candidate_aval_to, interviewer_aval_to)
        if not lower_bound.split('T')[0] == upper_bound.split('T')[0]:
            return Response(status=400, data={'message': 'Slots dont lie on same day'})
        lower_hour = int(parser.parse(lower_bound).strftime('%H'))
        upper_hour = int(parser.parse(upper_bound).strftime('%H'))
        intervals = [(l, l+1) for l in range(lower_hour, upper_hour)]
        return Response(intervals)
