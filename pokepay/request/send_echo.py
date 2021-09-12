from pokepay.request.request import PokepayRequest
from pokepay.response.echo import Echo


class SendEcho(PokepayRequest):
    def __init__(self, message):
        self.path = '/echo'
        self.method = 'POST'
        self.body_params = {'message': message}
        self.response_class = Echo
