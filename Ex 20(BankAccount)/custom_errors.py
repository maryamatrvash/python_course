class InsufficientFundsError(Exception):
    def __init__(self, msg="Funds Insufficient"):
        self.message = msg
        super().__init__(self.message) 


class AccountNumberError(Exception):
    def __init__(self, msg="Account Number Is Valid.Try Another Number!"):
        self.message = msg
        super().__init__(self.message) 