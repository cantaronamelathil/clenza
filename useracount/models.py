from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password, first_name=None,last_name=None,phone_number=None,role=None):
        
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have an username')
        
        user = self.model(
            email= self.normalize_email(email),
            username=username,
            phone_number= phone_number,
            first_name= first_name,
            last_name = last_name,
            role      = role,
            
        )
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email, username, password):
        user = self.create_user(email = self.normalize_email(email),
                                username =username,
                                password= password,)
        user.is_admin=True
        user.is_active =True
        user.is_staff= True
        user.is_superadmin=True
        user.role="ADMIN"
        user.save(using=self._db)
        return user
    
    
    # def create_vendor(self,email,username,password,phone_number,first_name,
    #         last_name ):
    #     user = self.create_user(email = self.normalize_email(email),
    #                             phone_number= phone_number,
    #                             username =username,
    #                             password= password,
    #                             first_name= first_name,
    #                             last_name = last_name,)   
    #     user.is_active = True
    #     user.is_vendor = True
    #     user.save(using=self._db)
    #     return user
    
class Accounts(AbstractBaseUser):
    class Roles(models.TextChoices):
        ADMIN ="ADMIN","Admin"
        CUSTOMER ="CUSTOMER","Customer"
        VENDOR = "VENDOR","Vendor"
        WORKER = "WORKER","worker"
    
    base_role = Roles.ADMIN
    
    
    
    first_name  = models.CharField(max_length=50, null=True, blank=True )
    last_name   = models.CharField(max_length=50, null=True,blank=True)
    role        = models.CharField(max_length=50,choices=Roles.choices)
    username    = models.CharField(max_length=50, unique=True)
    email       = models.EmailField(max_length=100, unique=True,blank=True, null=True, db_column='email')
    phone_number = models.CharField(max_length=50, null=True,blank=True)
    picture = models.ImageField(blank=True, null=True)

# required
    date_joined   = models.DateTimeField(auto_now_add=True)
    last_login    = models.DateTimeField(auto_now_add=True)
    is_admin      = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_vendor     = models.BooleanField(default=False)
    
    USERNAME_FIELD ='email'
    
    REQUIRED_FIELDS = ['username','password']
    
    objects = MyAccountManager()
    
    
    
    # def save(self,*args,**kwargs):
    #     if not self.pk:
    #         self.role = self.base_role
    #     return super().save(*args,**kwargs)
            
    
    def __str__(self):
        return self.email 

    
    def has_perm(self,perm,obj=None):
        return self.is_admin 

    def has_module_perms(self,add_label):
        return True
    
        
      
               
        