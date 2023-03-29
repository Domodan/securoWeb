from django.contrib import admin
# Register your models here.
from .models import TransactionTypeModel
#Register all Models
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display= ('transaction_type_id','transaction_type_name','created_on')#Display Data in A List
    search_fields = ('transaction_type_name','created_on',)#Add A search Field
#Register Models
admin.site.register(TransactionTypeModel,TransactionTypeAdmin)
