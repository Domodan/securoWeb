from django.conf.urls import url
from django.urls import path
from .views import TransactionTypesDetailApi,TransactionTypesApi,TransactionsApi,TransactionsDetailApi,WalletsApi,WalletsDetailApi
#Add Our API URLS
urlpatterns = [
    path('transaction-types/', TransactionTypesApi.as_view(),name="Transaction Types"),
    path('transaction-types/<int:id>/', TransactionTypesDetailApi.as_view(),name="Transaction Types Detail"),
    path('transactions/', TransactionsApi.as_view(),name="Transactions"),
    path('transactions/<int:id>/', TransactionsDetailApi.as_view(),name="Transactions Detail"),
    path('wallets/', WalletsApi.as_view(),name="Wallets"),
    path('wallets/<int:id>/', WalletsDetailApi.as_view(),name="Wallet Detail"),

]
