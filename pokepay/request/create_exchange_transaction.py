# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.request.request import PokepayRequest
from pokepay_partner_python_sdk.pokepay.response.transaction_detail import TransactionDetail


class CreateExchangeTransaction(PokepayRequest):
    def __init__(self, user_id, sender_private_money_id, receiver_private_money_id, amount, **rest_args):
        self.path = "/transactions" + "/exchange"
        self.method = "POST"
        self.body_params = {"user_id": user_id,
                            "sender_private_money_id": sender_private_money_id,
                            "receiver_private_money_id": receiver_private_money_id,
                            "amount": amount}
        self.body_params.update(rest_args)
        self.response_class = TransactionDetail
