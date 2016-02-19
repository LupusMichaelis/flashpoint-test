

from rest_framework import serializers
from models import Stats

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ('cities', 'users',)

