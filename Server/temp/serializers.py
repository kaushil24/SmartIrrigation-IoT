from rest_framework import serializers
from .models import Temp

class TempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temp
        fields = "__all__"