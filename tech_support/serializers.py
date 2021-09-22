from rest_framework import serializers
from .models import SpecialistsModel


class SpecialistsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialistsModel
        fields = '__all__'









