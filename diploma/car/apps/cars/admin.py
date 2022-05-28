from django.contrib import admin

from cars.models import (
    Car,
    Mark,
    Category,
)

class CarAdmin(admin.ModelAdmin):

    readonly_fields: tuple = (
        'datetime_deleted',
        'datetime_created',
        'datetime_updated',
    )

admin.site.register(Mark)
admin.site.register(Category)
admin.site.register(Car, CarAdmin)
