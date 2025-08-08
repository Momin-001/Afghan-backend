from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all().order_by('name')
    serializer_class = BusinessSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'address']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        province_id = self.request.query_params.get('province')

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if province_id:
            queryset = queryset.filter(province_id=province_id)
        return queryset

    # def get_serializer_class(self):
    #     category_id = self.request.query_params.get('category')
    #     province_id = self.request.query_params.get('province')

    #     if category_id or province_id:
    #         return BusinessCategorySerializer  
    #     return BusinessSerializer 
    
    @action(detail=False, methods=['get'], url_path='featured')
    def featured_businesses(self, request):
        featured = Business.objects.filter(featured=True)
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)

    #     if not queryset.exists():
    #         return Response({
    #             "success": False,
    #             "statuscode": status.HTTP_204_NO_CONTENT,
    #             "message": "No categories found",
    #             "data": []
    #         }, status=status.HTTP_200_OK)

    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_200_OK,
    #         "message": "Category list fetched successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_200_OK)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_200_OK,
    #         "message": "Category detail fetched successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_200_OK)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_201_CREATED,
    #         "message": "Category created successfully",
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
    #         "message": "Category updated successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_200_OK)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_204_NO_CONTENT,
    #         "message": "Category deleted successfully",
    #         "data": None
    #     }, status=status.HTTP_204_NO_CONTENT)


class ProvinceViewSet(viewsets.ModelViewSet):

    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)

    #     if not queryset.exists():
    #         return Response({
    #             "success": False,
    #             "statuscode": status.HTTP_204_NO_CONTENT,
    #             "message": "No Provinces found",
    #             "data": []
    #         }, status=status.HTTP_200_OK)

    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_200_OK,
    #         "message": "Provinces list fetched successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_200_OK)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_200_OK,
    #         "message": "Province detail fetched successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_200_OK)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_201_CREATED,
    #         "message": "Province created successfully",
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
    #         "message": "Province updated successfully",
    #         "data": serializer.data
    #     }, status=status.HTTP_200_OK)

    # def destroy(self, request, *args, **kwargs):

    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response({
    #         "success": True,
    #         "statuscode": status.HTTP_204_NO_CONTENT,
    #         "message": "Province deleted successfully",
    #         "data": None
    #     }, status=status.HTTP_204_NO_CONTENT)
    


