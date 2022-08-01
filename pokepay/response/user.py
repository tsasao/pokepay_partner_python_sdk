# DO NOT EDIT: File is generated by code generator.

from pokepay.response.response import PokepayResponse


class User(PokepayResponse):
    def __init__(self, response, response_body):
        super().__init__(response, response_body)
        self.id = response_body['id']
        self.name = response_body['name']
        self.is_merchant = response_body['is_merchant']

    def id(self):
        return self.id

    def name(self):
        return self.name

    def is_merchant(self):
        return self.is_merchant

