from typing import (
    Optional,
    Union,
)
from rest_framework.response import Response as DRF_Response


from abstracts.paginators import (
    AbstractPageNumberPaginator,
    AbstractLimitOffsetPaginator,
)



class JsonResponseMixin:
    """Mixin for handling JSON response rendering."""

    def get_json_response(
        self,
        data: Union[dict, str],
        paginator: Optional[
            Union[
                AbstractPageNumberPaginator,
                AbstractLimitOffsetPaginator,
            ]
        ] = None
    ) -> DRF_Response:
        """Get JSON response."""

        response: Optional[DRF_Response] = None

        if paginator:
            response = paginator.get_paginated_response(
                data
            )
        else:
            response = DRF_Response(
                {
                    'results': data
                }
            )
        return response
