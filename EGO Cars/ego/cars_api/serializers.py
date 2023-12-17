from rest_framework import serializers
from .models import Vehicle, Feature, Review, Concessionaire, TestDrivePetition, Service, Accesory, Activity
from django.utils import timezone
from datetime import time

class FeatureSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Feature
        fields = ['id','vehicle','name', 'description', 'image', 'primary_feature']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['type', 'model_name', 'brand', 'year', 'price', 'description', 'tagline', 'image', 'created_at', 'updated_at']
    
    def validate(self, data):
        if data['price'] < 0:
            raise serializers.ValidationError("Price must be a positive number")
        return data


class VehicleSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'model_name','type', 'year', 'price', 'image']


class ReviewSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = ['vehicle', 'client_name', 'client_email', 'description']


class ConcessionaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionaire
        fields = ['name', 'address', 'phone']
    
    def validate(self, data):
        # very simple validation, could be changed to fit the requirements
        # I'm assuming the phone number is in the format +XX XXX XXX XXX (area code) or XXX XXX XXX (regular) or XXXXXXX (landline)
        if len(data['phone'])>13 or len(data['phone'])<7:
            raise serializers.ValidationError("Phone number error")
        return data


class TestDrivePetitionSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(read_only=True)
    approved = serializers.BooleanField(read_only=True)
    class Meta:
        model = TestDrivePetition
        fields = '__all__'
    
    def validate(self, data):
        requested_date = data.get('requested_date')
        requested_time = data.get('requested_time')
        if requested_date and requested_date < timezone.now().date():
            raise serializers.ValidationError("Date must be in the future")
        if requested_time:
            if not (time(9, 0) <= requested_time <= time(17, 0)):  # Check if time is between 9 AM and 5 PM
                raise serializers.ValidationError("Time must be between 9 AM and 5 PM")
        return data

class TestDrivePetitionApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDrivePetition
        fields = ['approved']
    

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class AccesorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accesory
        fields = '__all__'
    
    def validate(self, data):
        if data['price'] < 0:
            raise serializers.ValidationError("Price must be a positive number")
        return data


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
