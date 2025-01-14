# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# # Create your models here.
# #This is the custom user for new to overwrite django default user.

# #for the custom manageer
# class CustomAccountManager(BaseUserManager):

#     def create_user(self, email, user_name, first_name, password, **other_fields):
#         if not email:
#             raise ValueError(_("You must provide an email address"))
        
#         email=self.normalize_email(email)
#         user=self.model(
#             email=email, user_name=user_name,
#             first_name=first_name, **other_fields
#         )
        
#         user.set_password(password)
#         user.save(using=self.db)
#         return user
   
#     def create_superuser(self, email, user_name, first_name, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active', True)
         
#         if extra_fields.get('is_staff') is not True:
#            raise ValueError(
#               'Superuser must be assigned to is_staff=True.')
 
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser= True.' )
        
#         return self.create_user(email, user_name, first_name, password, **extra_fields)
       
    
# #for custome user_models
# class NewUser(AbstractBaseUser,PermissionsMixin):
#     email=models.EmailField(_('email address'), unique=True)
#     user_name=models.CharField(max_length=150, unique=True)
#     first_name=models.CharField(max_length=150,blank=True)
#     start_date=models.DateTimeField(default=timezone.now)
#     about=models.TextField(_('about'),max_length=500, blank=True)
#     is_staff=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=True)

#     USERNAME_FIELD='email'
#     REQUIRED_FIELDS=['user_name','first_name']

#     objects=CustomAccountManager()

#     def _str_(self):
#         return self.user_name


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    user_name=models.CharField(max_length=150, unique=True)
    first_name=models.CharField(max_length=150,blank=True)
    start_date=models.DateTimeField(default=timezone.now)
    about=models.TextField(_('about'),max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['user_name','first_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.user_name