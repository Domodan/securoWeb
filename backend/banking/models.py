from django.db import models

#Disease Report Model
class TransactionTypeModel(models.Model):
    transaction_type_id=models.AutoField(primary_key=True)
    transaction_type_name=models.CharField(max_length=10)
    created_on= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Transaction Types'
