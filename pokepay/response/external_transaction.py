# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.response.response import PokepayResponse


class ExternalTransaction(PokepayResponse):
    def __init__(self, response, response_body):
        super().__init__(response, response_body)
        self.id = response_body['id']
        self.is_modified = response_body['is_modified']
        self.sender = response_body['sender']
        self.sender_account = response_body['sender_account']
        self.receiver = response_body['receiver']
        self.receiver_account = response_body['receiver_account']
        self.amount = response_body['amount']
        self.done_at = response_body['done_at']
        self.description = response_body['description']

    def id(self):
        return self.id

    def is_modified(self):
        return self.is_modified

    def sender(self):
        return self.sender

    def sender_account(self):
        return self.sender_account

    def receiver(self):
        return self.receiver

    def receiver_account(self):
        return self.receiver_account

    def amount(self):
        return self.amount

    def done_at(self):
        return self.done_at

    def description(self):
        return self.description

