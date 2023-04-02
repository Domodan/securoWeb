from django.db import models
from django.conf import settings
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

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
    def clean(self):
        if self.transaction_amount > 0:
            if self.transaction_type_id.transaction_type_name == 'Withdraw' or self.transaction_type_id.transaction_type_name == 'Send':
                # user = request.user
                wallet = WalletModel.objects.get(user=self.user)
                available_balance = wallet.available_balance
                if self.transaction_amount > available_balance:
                    raise ValidationError("You do not have enough balance to complete this transaction.")
        else:
            raise ValidationError("You can not use Negative values for the Transactions.")


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
    
  
# Receiver to update the wallet balance for every new transaction
@receiver(pre_save,sender=TransactionsModel)
def update_wallet_balance(sender,instance,**kwargs):
    # Check if the record is just being created
    if instance.transaction_id is None:
        # Get the user_id from the wallet model
        try:
            wallet_model = WalletModel.objects.get(user=instance.user)
        except WalletModel.DoesNotExist:
            # WalletModel instance does not exist for user
            return
        # Handle the Deposits
        if instance.transaction_type_id.transaction_type_name == 'Deposit':
            wallet_model.available_balance += instance.transaction_amount
            wallet_model.save()
        # handle the withdraws
        elif instance.transaction_type_id.transaction_type_name == 'Withdraw':
            wallet_model.available_balance -= instance.transaction_amount
            wallet_model.save()
        # handle the send money
        elif instance.transaction_type_id.transaction_type_name == 'Send':
            wallet_model.available_balance -= instance.transaction_amount
            wallet_model.save()
    else:
        print("Updating Transaction")
