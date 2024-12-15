from models.transaction import Transaction
from dtos import CreateTransactionDTO

class TransactionService:

    @staticmethod
    def create_transaction(createTransactionRequest: CreateTransactionDTO):
        transaction = Transaction(
            name=CreateTransactionDTO.name, 
            description=CreateTransactionDTO.description,
            amount=CreateTransactionDTO.amount,
            date=CreateTransactionDTO.date,
            transaction_type=CreateTransactionDTO.transaction_type)
        
        transaction.save()

        return transaction