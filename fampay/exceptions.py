from fampay.constants import PaginationError


class PaginationException(Exception):
    def __init__(
        self,
        code=PaginationError.PAGINATION_ERROR_RESPONSE_CODE,
        message=PaginationError.PAGINATION_ERROR_RESPONSE_MESSAGE,
    ):
        self.type = type
        super().__init__(code, message)