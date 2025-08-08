from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False, allow_null=True)
    image_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['id', 'updated_at', 'created_at', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None
    
    def create(self, validated_data):
        image = validated_data.pop('image', None)
        event = Event.objects.create(**validated_data)
        
        if image:
            event.image = image
            event.save()
        
        return event
    
    def update(self, instance, validated_data):

        image = validated_data.pop('image', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if image:
            instance.image = image
        
        instance.save()
        return instance