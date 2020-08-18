from django.contrib import admin

from .models import MasterLogger
# Register your models here.


@admin.register(MasterLogger)
class MasterLoggerAdmin(admin.ModelAdmin):
    list_display = ['email', 'login_cnt', 'last_login']
    readonly_fields = ('user', 'email', 'login_cnt',
                       'last_login', 'history_log')
