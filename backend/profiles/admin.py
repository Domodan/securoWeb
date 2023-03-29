from django.contrib import admin
# Register your models here.
from .models import UsersModel
#Register all Models
class UsersAdmin(admin.ModelAdmin):
    list_display= ('email','first_name','last_name','phone_number','is_active','is_staff','date_joined')#Display Data in A List
    search_fields = ('email','first_name','last_name','phone_number',)#Add A search Field
#Register Models
admin.site.register(UsersModel,UsersAdmin)
