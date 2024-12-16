class CreateTransactionDTO:

    def __init__(self, name, description, amount, transaction_type, date):
        self.name = name
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date