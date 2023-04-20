from django.conf.urls import url
from django.urls import path
from .views import TransactionTypesDetailApi,TransactionTypesApi
#Add Our API URLS
urlpatterns = [
    path('transaction-types/', TransactionTypesApi.as_view(),name="Transaction Types"),
    path('transaction-types/<int:id>/', TransactionTypesDetailApi.as_view(),name="Transaction Types Detail"),

]
