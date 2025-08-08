from django.db import models
from cloudinary.models import CloudinaryField

class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    img_link=models.URLField()

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    address = models.TextField()
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='businesses')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='businesses')

    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)

    map_location_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    featured = models.BooleanField(default=False)
    image = CloudinaryField('business_image', folder='business_images/', blank=True, null=True)

    def __str__(self):
        return self.name