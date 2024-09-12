from .models import Job, Category
from .serializers import JobSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import generics


class JobSerializerList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
class JobSerializerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'
    
    
    
class CategorySerializerList(generics.ListCreateAPIView):
    queryset = Category .objects.all()
    serializer_class = CategorySerializer
    
class CategorySerializerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'
    
    
    