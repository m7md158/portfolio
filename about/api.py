from .models import Skills
from .serializers import SkillsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


class SkillsList(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    
class SkillsDetail(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()
    lookup_field = 'id'