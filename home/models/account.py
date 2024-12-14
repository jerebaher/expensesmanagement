from django.db import models
from django.contrib.auth.models import User  

class Account(models.Model):
    name = models.CharField(max_length=20)  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    description = models.TextField(blank=True)  
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    
    def __str__(self):
        return f"{self.name} - Balance: {self.balance}"