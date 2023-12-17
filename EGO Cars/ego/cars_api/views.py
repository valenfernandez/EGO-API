from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer, FeatureSerializer, VehicleSummarySerializer, ReviewSerializer, ConcessionaireSerializer, TestDrivePetitionSerializer, ServiceSerializer, AccesorySerializer, ActivitySerializer, TestDrivePetitionApprovalSerializer
from .models import Vehicle, Feature, Review, Concessionaire, TestDrivePetition, Service, Accesory, Activity
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import FilterSet, NumberFilter
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import MethodNotAllowed
from django.contrib.auth.decorators import login_required
from copy import deepcopy
import logging
class VehicleViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class VehicleSummaryViewSet(generics.ListAPIView):
    lookup_field = 'id'
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSummarySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'model_name': ['exact'],
        'type': ['exact'],
    }
    ordering_fields = ['year', 'price']
    

class VehicleDetailView(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Retrieve all features associated with this vehicle
        features = Feature.objects.filter(vehicle=instance)
        feature_data = FeatureSerializer(features, many=True).data

        data = serializer.data
        data['features'] = feature_data

        return Response(data)

class VehicleFeaturesViewSet(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def list(self, request, *args, **kwargs):
        vehicle_id = self.kwargs.get('id')
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            logging.error("Vehicle not found")
            return Response({"detail": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
        
        queryset = Feature.objects.filter(vehicle=vehicle)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class VehicleKeyFeaturesViewSet(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def list(self, request, *args, **kwargs):
        vehicle_id = self.kwargs.get('id')
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            logging.error("Vehicle not found")
            return Response({"detail": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
        
        queryset = Feature.objects.filter(vehicle=vehicle, primary_feature=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    def create(self, request, *args, **kwargs):
        logging.error("Method POST not allowed in this endpoint")
        raise MethodNotAllowed('POST')


class AddFeatureToVehicleView(generics.UpdateAPIView):
    serializer_class = FeatureSerializer

    def put(self, request, *args, **kwargs):
        vehicle_id = self.kwargs.get('id')
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            logging.error("Vehicle not found")
            return Response({"detail": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
        
        feature_data = request.data
        feature_data['vehicle'] = vehicle_id # Asociar el Feature con el Vehicle
        
        feature_serializer = FeatureSerializer(data=feature_data)
        if feature_serializer.is_valid():
            feature_serializer.save(vehicle=vehicle)
            logging.info("Feature created successfully")
            return Response(feature_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(feature_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TestDriveRequests(generics.ListAPIView):
    queryset = TestDrivePetition.objects.all()
    serializer_class = TestDrivePetitionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'vehicle': ['exact'],
        'approved': ['exact'],
    }
    ordering_fields = ['requested_date', 'requested_time']


class RequestVehicleTestDriveView(generics.UpdateAPIView):
    serializer_class = TestDrivePetitionSerializer

    def put(self, request, *args, **kwargs):
        vehicle_id = self.kwargs.get('id')
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            logging.error("Vehicle not found")
            return Response({"detail": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
        
        test_drive_data = deepcopy(request.data)
        test_drive_data['vehicle'] = vehicle_id
        test_drive_serializer = TestDrivePetitionSerializer(data=test_drive_data)
        if test_drive_serializer.is_valid():
            test_drive_serializer.save(vehicle=vehicle)
            logging.info("Test drive petition created successfully")
            return Response(test_drive_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(test_drive_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ApproveTestDrive(generics.UpdateAPIView):
    queryset = TestDrivePetition.objects.all()
    serializer_class = TestDrivePetitionApprovalSerializer
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        test_drive_id = self.kwargs.get(self.lookup_url_kwarg)
        try:
            test_drive = TestDrivePetition.objects.get(pk=test_drive_id)
        except TestDrivePetition.DoesNotExist:
            logging.error("TestDrivePetition not found")
            return Response({"detail": "TestDrivePetition not found"}, status=status.HTTP_404_NOT_FOUND)
       
        # Update the 'approved' field
        test_drive.approved = request.data.get("approved")
        test_drive.save()

        serializer = self.get_serializer(test_drive, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    

class MakeReviewView(generics.UpdateAPIView):
    serializer_class = ReviewSerializer

    def put(self, request, *args, **kwargs):
        vehicle_id = self.kwargs.get('id')
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            logging.error("Vehicle not found")
            return Response({"detail": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
        
        review_data = deepcopy(request.data)
        review_data['vehicle'] = vehicle_id
        review_serializer = ReviewSerializer(data=review_data)
        if review_serializer.is_valid():
            review_serializer.save(vehicle=vehicle)
            logging.info("Review created successfully")
            return Response(review_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ReviewFilter(FilterSet):
    vehicle = NumberFilter(field_name='vehicle_id')

    class Meta:
        model = Review
        fields = ['vehicle']


class VehicleReviewsView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ReviewFilter 

    ordering_fields = ['created_at']


class ConcessionaireViewSet(viewsets.ModelViewSet):
    queryset = Concessionaire.objects.all()
    serializer_class = ConcessionaireSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AccesoryViewSet(viewsets.ModelViewSet):
    queryset = Accesory.objects.all()
    serializer_class = AccesorySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

