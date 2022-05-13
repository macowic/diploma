from rest_framework.permissions import BasePermission
from rest_framework.request import Request as DRF_Request


class CarPermission(BasePermission):
    """Determines permission for Car."""

    def __init__(self) -> None:
        self._admin: bool = False
        self._user: bool = False

    def _initialize_permissions(
        self,
        request: DRF_Request
    ) -> None:
        """Initializing base permissions."""

        self._user = (
            request.user and
            request.user.is_active
        )
        self._admin = self._user and (
            request.user.is_staff and
            request.user.is_superuser
        )

    def has_permission(
        self,
        request: DRF_Request,
        view: 'Car'
    ) -> bool:
        """Has permissions."""

        self._initialize_permissions(
            request
        )
        if view.action in (
            'list',
            'retrieve',
            'create',
            'partial_update',
            'update',
        ):
            return self._user

        if view.action in (
            'destroy',
        ):
            return self._admin

        return False
    
    
class CategoryPermission(BasePermission):
    """Determines permission for Car."""

    def __init__(self) -> None:
        self._admin: bool = False
        self._user: bool = False

    def _initialize_permissions(
        self,
        request: DRF_Request
    ) -> None:
        """Initializing base permissions."""

        self._user = (
            request.user and
            request.user.is_active
        )
        self._admin = self._user and (
            request.user.is_staff and
            request.user.is_superuser
        )

    def has_permission(
        self,
        request: DRF_Request,
        view: 'Category'
    ) -> bool:
        """Has permissions."""

        self._initialize_permissions(
            request
        )
        if view.action in (
            'list',
            'retrieve',
            'create',
            'partial_update',
            'update',
        ):
            return self._user

        if view.action in (
            'destroy',
        ):
            return self._admin

        return False

