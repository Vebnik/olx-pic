import urllib.request as req
from http.client import HTTPResponse


from src.http.models import HttpResponse


class Request:

    @staticmethod
    def post(url: str) -> HttpResponse:
        ...

    @staticmethod
    def get(url: str) -> HttpResponse:
        try:
            response: HTTPResponse = req.urlopen(url)

            return HttpResponse({
                'status': response.status,
                'reason': response.reason,
                'data': response.read().decode('utf-8')
             })
        except Exception as ex:
            return HttpResponse({ 'status': False, 'reason': ex, 'data': None, })
        
    @staticmethod
    def load_data(url: str, name: str|int, path: str) -> None:
        try:
            req.urlretrieve(url, f'{path}/item_{name}.jpeg')
        except Exception as ex:
            print(ex)