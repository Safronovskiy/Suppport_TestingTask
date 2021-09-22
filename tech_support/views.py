from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SpecialistsModel
from .serializers import SpecialistsSerializer



class SpecialistsModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing specialists.
    """
    queryset = SpecialistsModel.objects.all()
    serializer_class = SpecialistsSerializer
    permission_classes =[]