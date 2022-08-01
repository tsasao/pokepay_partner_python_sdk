# DO NOT EDIT: File is generated by code generator.

from pokepay.response.response import PokepayResponse


class PrivateMoney(PokepayResponse):
    def __init__(self, response, response_body):
        super().__init__(response, response_body)
        self.id = response_body['id']
        self.name = response_body['name']
        self.unit = response_body['unit']
        self.is_exclusive = response_body['is_exclusive']
        self.description = response_body['description']
        self.oneline_message = response_body['oneline_message']
        self.organization = response_body['organization']
        self.max_balance = response_body['max_balance']
        self.transfer_limit = response_body['transfer_limit']
        self.type = response_body['type']
        self.expiration_type = response_body['expiration_type']
        self.enable_topup_by_member = response_body['enable_topup_by_member']
        self.display_money_and_point = response_body['display_money_and_point']

    def id(self):
        return self.id

    def name(self):
        return self.name

    def unit(self):
        return self.unit

    def is_exclusive(self):
        return self.is_exclusive

    def description(self):
        return self.description

    def oneline_message(self):
        return self.oneline_message

    def organization(self):
        return self.organization

    def max_balance(self):
        return self.max_balance

    def transfer_limit(self):
        return self.transfer_limit

    def type(self):
        return self.type

    def expiration_type(self):
        return self.expiration_type

    def enable_topup_by_member(self):
        return self.enable_topup_by_member

    def display_money_and_point(self):
        return self.display_money_and_point

