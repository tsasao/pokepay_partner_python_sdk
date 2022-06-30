# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.request.request import PokepayRequest
from pokepay_partner_python_sdk.pokepay.response.account_deleted import AccountDeleted


class DeleteAccount(PokepayRequest):
    def __init__(self, account_id, **rest_args):
        self.path = "/accounts" + "/" + account_id
        self.method = "DELETE"
        self.body_params = {}
        self.body_params.update(rest_args)
        self.response_class = AccountDeleted
