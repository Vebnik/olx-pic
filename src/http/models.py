
class HttpResponse:

    status: int
    reason: str
    data: dict|str

    def __init__(self, response) -> None:
        self.status = response.get('status')
        self.reason = response.get('reason')
        self.data = response.get('data')

    def __str__(self) -> str:
        return f'status: {self.status} reason: {self.reason} data: {len(self.data) if self.data else "empty"}'