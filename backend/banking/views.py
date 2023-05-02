from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TransactionTypeSerializer,UpdateTransactionTypeSerializer,TransactionsSerializer,UpdateTransactionsSerializer,WalletSerializer,UpdateWalletsTypeSerializer
#Import all the models
from .models import WalletModel,TransactionsModel,TransactionTypeModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



#Class to Manage Transaction Types
class TransactionTypesApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=UpdateTransactionTypeSerializer(data=request.data)
        if item.is_valid():
            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'message': 'Record Created successfully',
                }
                return Response(response,status=status_code)
        return Response(item.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = TransactionTypeModel.objects.all().order_by('created_on')
        serializer_class = TransactionTypeSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific 
class TransactionTypesDetailApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = TransactionTypeModel.objects.filter(transaction_type_id=id)
            serializer_class = UpdateTransactionTypeSerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status_code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status_code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = TransactionTypeModel.objects.filter(transaction_type_id=id).first()
        serializer_class = UpdateTransactionTypeSerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

#Class to Manage Transactions
class TransactionsApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=UpdateTransactionsSerializer(data=request.data)
        if item.is_valid():
            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'message': 'Record Created successfully',
                }
                return Response(response,status=status_code)
        return Response(item.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = TransactionsModel.objects.all().order_by('transaction_date')
        serializer_class = TransactionsSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific 
class TransactionsDetailApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = TransactionsModel.objects.filter(user=id)
            serializer_class = UpdateTransactionsSerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status_code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status_code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = TransactionsModel.objects.filter(transaction_id=id).first()
        serializer_class = UpdateTransactionsSerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)


#Class to Manage Transactions
class WalletsApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=UpdateWalletsTypeSerializer(data=request.data)
        if item.is_valid():
            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'message': 'Record Created successfully',
                }
                return Response(response,status=status_code)
        return Response(item.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = WalletModel.objects.all().order_by('wallet_update_date')
        serializer_class = WalletSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific 
class WalletsDetailApi(APIView):
    permission_classes = (AllowAny,)
    #authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = WalletModel.objects.filter(user=id)
            serializer_class = UpdateWalletsTypeSerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status_code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status_code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = WalletModel.objects.filter(user=id).first()
        serializer_class = UpdateWalletsTypeSerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)