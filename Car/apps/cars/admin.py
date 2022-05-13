from pyexpat import model
from django.contrib import admin

from .models import (
    Car,
    Category,
    Mark
)

class CarAdmin(admin.ModelAdmin):
    model = Car
    readonly_fields = (
        'datetime_deleted',
        'datetime_created',
        'datetime_updated',
    )

admin.site.register(Car, CarAdmin)
admin.site.register(Category)
admin.site.register(Mark)
