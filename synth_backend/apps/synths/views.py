from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SynthSerializer
from .models import Synths
# Create your views here.

class SynthViewSet(viewsets.ModelViewSet):
    queryset = Synths.objects.all()
    serializer_class = SynthSerializer
    
    def get_queryset(self):
        return self.get_queryset().filter(create_by=self.request.user)

