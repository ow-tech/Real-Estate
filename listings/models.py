from django.db import models
from datetime import datetime
from realtors.models import Realtor
from cloudinary.models import CloudinaryField


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    # address = models.CharField(max_length=200)
    developer = models.CharField(max_length=200, blank=True)
    area = models.CharField(max_length=100)
    amenities = models.CharField(max_length=200, null=True)
    kids_facilities = models.CharField(max_length=200, null=True)
    sports_facilities = models.CharField(max_length=200, null=True)
    swimming_pool = models.CharField(max_length=200, null=True)
    highlights = models.CharField(max_length=200, null=True)
    furnished = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    # bedrooms = models.IntegerField()
    # bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    # garage = models.IntegerField(default=0)
    # sqft = models.IntegerField()
    # lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    
    is_published = models.BooleanField(default=True)
    PROPERTY_STAGES = [
        ("READY", "Ready to Move In"),
    ("MORTGAGE", "Mortgage Plan / OffPlan")
        
    ]

    property_status = models.CharField(max_length=9,
                  choices=PROPERTY_STAGES,
                  default="READY")
    is_handOver_in_12_months = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    is_villas_and_mansionettes = models.BooleanField(default=False)
    photo_main =CloudinaryField('image', blank=True)
    photo_1 = CloudinaryField('image', blank=True)
    photo_2 = CloudinaryField('image', blank=True)
    photo_3 = CloudinaryField('image', blank=True)
    photo_4 = CloudinaryField('image', blank=True)
    photo_5 = CloudinaryField('image', blank=True)
    photo_6 = CloudinaryField('image', blank=True)
    photo_7 = CloudinaryField('image', blank=True)
    photo_8 = CloudinaryField('image', blank=True)
    photo_9 = CloudinaryField('image', blank=True)
    photo_10 = CloudinaryField('image', blank=True)
    photo_11 = CloudinaryField('image', blank=True)
    photo_12 = CloudinaryField('image', blank=True)
    
    
    
    list_date = models.DateTimeField(default=datetime.now, blank=True)
  
    

    def __str__(self):
        return self.title
    
class Floor_Plan(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bedrooms =models.IntegerField(blank=True, null=True)
    is_studio = models.BooleanField(default=False)
    price_sqft =models.IntegerField(blank=True, null=True)
    from_sqft =models.IntegerField(blank=True, null=True)
    min_price =models.IntegerField(blank=True, null=True)
    floor_plan_image= CloudinaryField('image', blank=True)
    
    
    def __int__(self):
        return self.bedrooms
    
    

