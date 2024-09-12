from .models import WorkExperience, Education
from .serializers import WorkExperienceSerializer, EducationSerializer
from rest_framework.response import Response
from rest_framework import generics


class WorkExperienceList(generics.ListCreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    
class WorkExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkExperienceSerializer
    queryset = WorkExperience.objects.all()
    lookup_field = 'id'
    
    
class EducationSerializerList(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
class EducationSerializerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()
    lookup_field = 'id'