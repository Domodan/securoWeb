from django.db import models
from django.conf import settings

#Transaction Type Model
class TransactionTypeModel(models.Model):
    transaction_type_id=models.AutoField(primary_key=True)
    transaction_type_name=models.CharField(unique=True,max_length=10)
    created_on= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Transaction Types'
    def __str__(self):
        return self.transaction_type_name
        
#Transactions Model
class TransactionsModel(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transaction_type_id=models.ForeignKey(TransactionTypeModel,on_delete=models.CASCADE)
    transaction_amount=models.BigIntegerField(default=0)
    transaction_desc=models.TextField(blank=True)
    transaction_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = 'Transactions'

#Wallet Model
class WalletModel(models.Model):
    wallet_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    available_balance=models.BigIntegerField(default=0)
    wallet_update_date= models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = 'Wallets'  
    def __str__(self):
        return self.user.get_full_name() 
