from .models import Service
from . serializers import ServiceSerializer
from rest_framework.response import Response
from rest_framework import generics


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = 'id'