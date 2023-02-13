from django.db import models
from django.contrib.auth.models import BaseUserManager
from useracount.models import Accounts
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_vendor(self, username, email, phone_number, address, firm_name, services, password=None):
        vendor = self.model(username=username, email=self.normalize_email(email), phone_number=phone_number, address=address, firm_name=firm_name, services=services, is_vendor=True)
        vendor.set_password(password)
        vendor.save(using=self.db)
        return vendor
class Vendor(Accounts):
    address = models.TextField()
    firm_name = models.CharField(max_length=100)
    services = models.TextField()
    
    
    
    REQUIRED_FIELDS = ['email','password']
    
    object = MyAccountManager()
    
    def __str__(self):
        return self.firm_name
    
    def has_perm(self,perm,obj=None):
        return self.is_vendor

    def has_module_perms(self,add_label):
        return True
    
    
    
