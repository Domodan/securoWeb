# serializers.py --This file will serialize all the data of this app
from rest_framework import serializers #import the serializer
from .models import WalletModel,TransactionsModel,TransactionTypeModel

#Transaction Type Serializers for Create, Get,Delete
class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTypeModel
        fields = ('transaction_type_id', 'transaction_type_name','created_on')
        transaction_type_id = serializers.IntegerField()
        transaction_type_name = serializers.CharField(max_length=10)
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
#Transaction Type Serializers for Update
class UpdateTransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTypeModel
        fields = ('transaction_type_id', 'transaction_type_name','created_on')
        transaction_type_id = serializers.IntegerField()
        transaction_type_name = serializers.CharField(max_length=10)