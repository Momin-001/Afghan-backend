from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from .models import *
from .serializers import *
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)

    #     if not queryset.exists():
    #         return Response({
    #             "success": False,
    #             "statuscode": status.HTTP_204_NO_CONTENT,
    #             "message": "No Events found",
    #             "data": []
    #         }, status=status.HTTP_200_OK)

    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_200_OK,
    #         "message": "Events fetched successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_200_OK)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_200_OK,
    #         "message": "Event detail fetched successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_200_OK)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_201_CREATED,
    #         "message": "Event created successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_200_OK,
    #         "message": "Event updated successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_200_OK)

    # def destroy(self, request, *args, **kwargs):

    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_204_NO_CONTENT,
    #         "message": "Event deleted successfully",
    #         "data": None
    #     }, status=status.HTTP_204_NO_CONTENT)