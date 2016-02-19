from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from models import Stats

def index():
    pass

@api_view(['GET'])
def stat(r):
    try:
        data = Stats.objects.get()
        serializer = serializers.Serializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Stats.DoesNotExist:
        payload = { 'result':'error', 'error':'Stat unavailable' }
        return Response(payload, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
