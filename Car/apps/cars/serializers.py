from dataclasses import fields
from unicodedata import category
from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    DateTimeField
)
from cars.models import (
    Car,
    Category
)


class CarSerializer(ModelSerializer):
    """CarSerializer."""

    mark = CharField(read_only=True)
    model = CharField(read_only=True)
    category = CharField(read_only=True)
    speed = IntegerField(read_only=True)
    motor = CharField(read_only=True)
    datetime_created = DateTimeField(read_only=True)
    datetime_updated = DateTimeField(read_only=True)
    datetime_deleted = DateTimeField(read_only=True)

    class Meta:
        model = Car
        fields = (
            'mark',
            'model',
            'category',
            'speed',
            'motor',
            'datetime_created',
            'datetime_updated',
            'datetime_deleted',
        )
        
class CategorySerializer(ModelSerializer):
    
    category = CharField(read_only=True)
    
    class Meta:
        model = Category
        fields = (
            'category',
        )
        