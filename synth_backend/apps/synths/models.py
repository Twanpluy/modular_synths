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
    file_name = models.CharField(max_length=1000, blank=True)
    file_path = models.CharField(max_length=1000, blank=True)    
    
    def __str__(self):
        return self.name , self.brand
    
    
class Ebay_Synths(models.Model):
    item_id = models.CharField(max_length=1000)
    synth_id = models.ForeignKey(Synths, on_delete=models.CASCADE, related_name='ebay_synths')
    title = models.CharField(max_length=1000)
    categoryname = models.CharField(max_length=1000)
    selling_status = models.CharField(max_length=1000)
    cost = models.CharField(max_length=1000)
    item_currency = models.CharField(max_length=1000)
    shipping_cost = models.CharField(max_length=1000)      
    shipping_to = models.CharField(max_length=1000)  
    shipping_currency = models.CharField(max_length=1000)
    condition = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    watcher_count = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    
    
    
    
    
    
    
    
    
    