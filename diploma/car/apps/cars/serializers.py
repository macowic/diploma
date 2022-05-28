from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
)

from cars.models import (
    Car,
    Category,
    Mark
)

class CarListSerializer(ModelSerializer):
    '''Cars list serializer'''

    mark = CharField(read_only=True)
    category = CharField(read_only=True)

    class Meta:

        model = Car
        fields = (
            'id',
            'mark',
            'model',
            'category',
        )

class CarDetailsSerializer(ModelSerializer):
    '''Car details serializer'''

    mark = CharField(read_only=True)
    category = CharField(read_only=True)

    class Meta:

        model = Car
        exclude = (
            'datetime_updated',
            'datetime_created',
            'datetime_deleted',
        )

class CategoryListSerializer(ModelSerializer):
    '''Categories list serializer'''

    category = CharField(read_only=True)

    class Meta:

        model = Category
        fields = (
            'id',
            'category',
        )

class CategoryDetailsSerializer(ModelSerializer):
    '''Categories details serializer'''

    mark = CharField(read_only = True)
    category = CharField(read_only=True)

    class Meta:

        model = Car
        fields = (
            'category',
            'mark',
            'model',
            'speed',
            'motor'
        )