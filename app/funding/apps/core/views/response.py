from rest_framework.response import Response
from rest_framework import status as drf_status
from typing import Optional


__all__ = [
        'get_status_by_code',
        'HttpStatus',
        'GenericResponse',
        ]


def get_status_by_code(status_code):
    _status = vars(drf_status)
    try:
        idx = list(_status.values()).index(status_code)
        return list(_status.keys())[idx]
    except ValueError:
        raise ValueError


class HttpStatus:
    """
    rest_framework status의 status code 기반으로 status와 code, custom message를 갖고 있는 object
    """
    def __init__(self, status_code, message=None, error=None):
        self.code = status_code
        try:
            self.status = get_status_by_code(status_code)
        except:
            self.status = None
        self.message = message
        if error is not None:
            self.message = error.message
            self.errors = error.params
            try:
                self.status = error.code
            except AttributeError:
                pass


class GenericResponse(Response):
    """
    import GenericResponse as Response\n
    Response 객체를 받아서 data형식에 맞게 변환시켜 전달한다\n
    생성자 인자로는 data와 HttpStatus를 받는다. -> Response(data, HttpStatus(400))\n
    기존 Response 객체와 유사하게 사용하여도 된다. (추천 사항은 아님) -> Response(data={}, status=status.HTTP_200_OK)\n
    4xx 혹은 5xx status의 경우 data 대신 errors를 전달해야 한다.
    """
    def __init__(self, data=None, http: Optional[HttpStatus]=None, status=None, **kwargs):
        self.status = status

        if isinstance(http, HttpStatus):
            status_code = http.code
            if drf_status.is_client_error(status_code) or drf_status.is_server_error(status_code):
                data_format = {
                    "code": status_code,
                    "status": http.status,
                    "message": http.message,
                    "errors": http.errors
                }
            else:
                data_format = {
                    "code": status_code,
                    "status": http.status,
                    "message": http.message,
                    "data": data
                }

            if self.status is None:
                super().__init__(
                    data_format, status_code, **kwargs
                )
            else:
                super().__init__(
                    data_format, self.status, **kwargs
                )
        elif isinstance(http, int):
            assert "http type is HttpStatus not int"
        else:
            super().__init__(data, **kwargs)
