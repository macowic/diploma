from typing import Optional
from unicodedata import category

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request
from rest_framework.permissions import AllowAny


from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from abstracts.validators import APIValidator
from abstracts.paginators import (
    AbstractPageNumberPaginator,
    AbstractLimitOffsetPaginator,
)
from abstracts.validators import APIValidator
from abstracts.mixins import JsonResponseMixin

from cars.models import (
    Car,
    Category,
    Mark
)
from cars.serializers import (
    CarListSerializer,
    CarDetailsSerializer,
    CategoryListSerializer,
    CategoryDetailsSerializer
)

class CarsViewSet(JsonResponseMixin,ModelViewSet):
    '''Cars ViewSet'''

    queryset: QuerySet[Car] = Car.objects.all()
    pagination_class: AbstractPageNumberPaginator = \
    AbstractPageNumberPaginator
    serializer_class: CarListSerializer = \
    CarListSerializer
    
    def get_queryset(self):
        return self.queryset.all()

    def list(self, request: DRF_Request) -> DRF_Response:
        cars = self.get_queryset()
        serializer: CarListSerializer = CarListSerializer(cars, many=True)
        return self.get_json_response(serializer.data)

    def retrieve(
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response:
        cars: Optional[Car] = None
        try:
            cars = self.get_queryset().get(
                id=pk
            )
        except Exception:
            return self.get_json_response(
                'Нет такой машины'
            )
        serializer: CarDetailsSerializer = \
            CarDetailsSerializer(
                cars,
            )
        return self.get_json_response(
            serializer.data
        )

class CategoryViewSet(JsonResponseMixin, ModelViewSet):
    '''Categories ViewSet'''

    permission_classes: tuple = (
        AllowAny,
    )

    queryset = Category.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    pagination_class: AbstractPageNumberPaginator = \
    AbstractPageNumberPaginator
    serializer_class: CategoryListSerializer = \
    CategoryListSerializer

    def list(self, request: DRF_Request) -> DRF_Response:
        categories =  self.get_queryset()
        serializer: CategoryListSerializer = CategoryListSerializer(categories, many=True)
        return self.get_json_response(serializer.data)

    def retrieve(
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response:
        cars: Optional[Car] = None
        try:
            cars = Car.objects.all().filter(category_id=pk)
        except Exception:
            return self.get_json_response(
                'Нет такой категории'
            )
        serializer: CategoryDetailsSerializer = \
        CategoryDetailsSerializer(cars, many=True)
        return self.get_json_response(serializer.data)