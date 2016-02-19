from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from models import Stats
from serializers import StatSerializer

def index():
    pass

@api_view(['GET'])
def stat(r):
    try:
        data = Stats.objects.get()
        serializer = StatSerializer(data)
        payload = {'result': 'success'}
        payload.update(serializer.data)
        return Response(payload)
    except Stats.DoesNotExist:
        payload = { 'result':'error', 'error':'Stat unavailable' }
        return Response(payload, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
