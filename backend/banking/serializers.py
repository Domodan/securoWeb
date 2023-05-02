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

#Transactions Serializers for Create, Get,Delete
class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionsModel
        fields = ('transaction_id', 'user','transaction_type_id','transaction_amount','transaction_desc','transaction_date')
        transaction_id = serializers.IntegerField()
        user = serializers.IntegerField()
        transaction_type_id = serializers.IntegerField()
        transaction_amount = serializers.IntegerField()
        transaction_desc = serializers.CharField()
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
#Transaction  Serializers for Update
class UpdateTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionsModel
        fields = ('transaction_id', 'user','transaction_type_id','transaction_amount','transaction_desc','transaction_date')
        transaction_id = serializers.IntegerField()
        user = serializers.IntegerField()
        transaction_type_id = serializers.IntegerField()
        transaction_amount = serializers.IntegerField()
        transaction_desc = serializers.CharField()
        
#Transactions Serializers for Create, Get,Delete
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletModel
        fields = ('wallet_id', 'user','available_balance','wallet_update_date')
        wallet_id = serializers.IntegerField()
        available_balance = serializers.IntegerField()
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
#Transaction  Serializers for Update
class UpdateWalletsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletModel
        fields = ('wallet_id', 'user','available_balance','wallet_update_date')
        wallet_id = serializers.IntegerField()
        available_balance = serializers.IntegerField()