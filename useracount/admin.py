from django.contrib import admin
from useracount.models import Accounts
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Accounts)