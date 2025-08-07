from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'img_link']

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name']

class BusinessSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(write_only=True, required=False, allow_null=True)
    image_url = serializers.SerializerMethodField(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Business
        fields = '__all__'
        read_only_fields = ['id', 'updated_at', 'created_at', 'image_url']
    
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None
    
    def create(self, validated_data):
        image = validated_data.pop('image', None)
        business = Business.objects.create(**validated_data)
        
        if image:
            business.image = image
            business.save()
        
        return business
    
    def update(self, instance, validated_data):

        image = validated_data.pop('image', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if image:
            instance.image = image
        
        instance.save()
        return instance
    

class BusinessCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Business
        fields = ['id', 'name']
        read_only_fields = ['id', 'name']