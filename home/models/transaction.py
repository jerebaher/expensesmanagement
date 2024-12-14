from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    )
    
    name = models.CharField(max_length=20)  
    description = models.CharField(max_length=100)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE)
    date = models.DateTimeField(auto_now_add=True)  
    account = models.ForeignKey('Account', on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.name} - {self.transaction_type} - {self.amount} - {self.date}"