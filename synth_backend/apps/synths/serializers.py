from rest_framework import serializers

from .models import Synths

#Create a serializer class
class SynthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synths
        read_only_fields = ('create_by', 'create_at', 'modified_by', 'modified_at'),
        fields = (
               'name',
               'brand',
               'type',
               'mode',
               'image',
               'description',
               'url'
        )
        
        
