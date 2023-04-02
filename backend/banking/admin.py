from django.contrib import admin
# Register your models here.
from .models import TransactionTypeModel,WalletModel,TransactionsModel
#Custom Django Admin
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display= ('transaction_type_id','transaction_type_name','created_on')#Display Data in A List
    list_filter = ('created_on',)
    search_fields = ('transaction_type_name','created_on',)#Add A search Field
class WalletAdmin(admin.ModelAdmin):
    exclude = ('available_balance',)
    list_display= ('wallet_id','user_full_name','available_balance','wallet_update_date')#Display Data in A List
    list_filter = ('wallet_update_date',)
    search_fields = ('user','available_balance',)#Add A search Field
    def user_full_name(self, obj):
        return obj.user.get_full_name()

    user_full_name.admin_order_field = 'user__first_name'
    user_full_name.short_description = 'User'
class TransactionsAdmin(admin.ModelAdmin):
    list_display= ('transaction_id','user_full_name','transaction_type_id','transaction_amount','transaction_date')#Display Data in A List
    list_filter = ('transaction_date',)
    search_fields = ('user_full_name','user_full_name',)#Add A search Field
    def user_full_name(self, obj):
        return obj.user.get_full_name()

    user_full_name.admin_order_field = 'user__first_name'
    user_full_name.short_description = 'User'
#Register Models
admin.site.register(TransactionTypeModel,TransactionTypeAdmin)
admin.site.register(WalletModel,WalletAdmin)
admin.site.register(TransactionsModel,TransactionsAdmin)
