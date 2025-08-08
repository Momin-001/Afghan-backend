from django.db import models
from cloudinary.models import CloudinaryField

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    venue = models.CharField(max_length=255)
    date = models.DateTimeField()
    website = models.URLField(blank=True, null=True)
    contact_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    image = CloudinaryField('event_image', folder='event_images/')

    def __str__(self):
        return f"{self.name} at {self.venue} on {self.date.strftime('%Y-%m-%d')}"
