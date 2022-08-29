from django.contrib import admin
from apps.account.models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display       = ('email', 'last_login', 'is_active','is_superuser')
    list_display_links = ('email',)
    ordering           = ('last_login',)
   
    filter_horizontal  = ()
    list_filter        = ()
    fieldsets          = () 


admin.site.register(Account,AccountAdmin)
