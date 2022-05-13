from typing import Any

from rest_framework.routers import DefaultRouter
from apps.cars.views import CarsViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.contrib import admin
from django.conf import settings
from django.urls import (
    path,
    include,
)
from django.conf.urls.static import static

from auths.views import (
    CustomUserViewSet,
)

from cars.views import (
    CarsViewSet,
)


urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]


# ------------------------------------------------
# API-Endpoints
#
router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register('auths', CustomUserViewSet)
router.register('cars', CarsViewSet)

urlpatterns += [
    path(
        'api/v1/',
        include(router.urls)
    ),
    path(
        'api/v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/v1/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
]
