from rest_framework.response import Response


class ApiResponse(Response):

    def __init__(
        self,
        data=None,
        message="Success",
        success=True,
        status=200,
        errors=None,
        **kwargs
    ):

        response = {
            "success": success,
            "message": message,
            "data": data,
            "errors": errors
        }

        super().__init__(
            data=response,
            status=status,
            **kwargs
        )