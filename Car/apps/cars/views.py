from typing import Optional
from datetime import datetime

from rest_framework.permissions import (
    AllowAny,
)

from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

from abstracts.validators import APIValidator
from abstracts.paginators import (
    AbstractPageNumberPaginator,
    AbstractLimitOffsetPaginator,
)
from abstracts.validators import APIValidator
from abstracts.mixins import JsonResponseMixin
from apps.cars.permissions import CategoryPermission

from cars.models import (
    Car,
    Category
)
from cars.serializers import (
    CarSerializer,
    CategorySerializer
)
from cars.permissions import CarPermission


class CarsViewSet(JsonResponseMixin,ViewSet):
    
    permission_classes: tuple = (
        CarPermission,
    )
    queryset: QuerySet[Car] = Car.objects.all()
    
    serializer_class: CarSerializer = CarSerializer
    
    pagination_class: AbstractPageNumberPaginator = AbstractPageNumberPaginator
    
    def get_queryset(self):
        return self.queryset.all()

    @action(
        methods=['get'],
        detail=False,
        permission_classes=(
            AllowAny,
        )
    )
    def list(self, request: DRF_Request) -> DRF_Response:
        
        paginator: AbstractPageNumberPaginator = self.pagination_class()
        
        objects: list = paginator.paginate_queryset(
            self.get_queryset(),
            request
        )
        serializer: CarSerializer =self.serializer_class(objects,many=True)
        return self.get_json_response(
            serializer.data,
            paginator
        )
        
    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        
        car: Optional[Car] = None
        try:
            car = self.get_queryset().get(
                id=pk
            )
        except Car.DoesNotExist:
            return self.get_json_response(
                'Не нашел такого юзера'
            )
        serializer: CarSerializer = \
            CarSerializer(
                car
            )
        return self.get_json_response(
            serializer.data
        )
        
class CategoryViewSet(JsonResponseMixin,ViewSet):
    
    permission_classes: tuple = (
        CategoryPermission,
    )
    queryset: QuerySet[Category] = Category.objects.all()
    
    serializer_class: CategorySerializer = CategorySerializer
    
    pagination_class: AbstractPageNumberPaginator = AbstractPageNumberPaginator
    
    
    def get_queryset(self):
        return self.queryset.all()

    @action(
        methods=['get'],
        detail=False,
        permission_classes=(
            AllowAny,
        )
    )
    def list(self, request: DRF_Request) -> DRF_Response:
        
        paginator: AbstractPageNumberPaginator = self.pagination_class()
        
        objects: list = paginator.paginate_queryset(
            self.get_queryset()
            request
        )
        serializer: CarSerializer =self.serializer_class(objects,many=True)
        return self.get_json_response(
            serializer.data,
            paginator
        )
        
    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        
        
        
    
        