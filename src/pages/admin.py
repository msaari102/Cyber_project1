from django.contrib import admin

from .models import Message, Account

admin.site.register(Message)
admin.site.register(Account)
