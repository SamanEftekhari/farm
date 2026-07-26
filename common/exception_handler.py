from rest_framework.views import exception_handler

from .api_response import ApiResponse


def custom_exception_handler(exc, context):

    response = exception_handler(
        exc,
        context
    )

    if response is None:
        return response

    return ApiResponse(
        success=False,
        message="Request failed.",
        errors=response.data,
        status=response.status_code
    )