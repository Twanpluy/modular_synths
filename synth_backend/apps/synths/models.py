from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Synths(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=100, blank=True)
    mode = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='synths')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    modified_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name