# from django.contrib import admin
# from users.models import NewUser
# from django.contrib.auth.admin import UserAdmin
# from django.forms import Textarea,CharField
# from django import forms
# from django.db import models
# Register your models here.

#create userAdmin
# class UserAdminConfig(UserAdmin):
#     model=NewUser
#     search_fields=('email','user_name',
#                    'first_name',)
#     list_filter=('email','user_name',
#                  'is_active', 'is_staff')
#     ordering=('-start_date',)
#     list_display=('email','id','user_name','first_name',
#                   'is_active','is_staff')
#     fieldsets=(
#         (None,{'fields':('email','user_name','first_name',)}),
#         ('Permission',{'fields':('is_staff','is_active')}),
#         ('Personal',{'fields':('about',)})
#     )
#     formatfield_overrides={
#        models.TextField:{'widget':Textarea(attrs={'rows':20,'cols':60})}
#     }
#     add_fieldsets=(
#         None,{
#         'classes':('wide'),
#         'fields':('email','user_name','first_name','password1','password2','is_active'),
#     },
#       )
    
# admin.site.register(NewUser)     
# 
# # from django.contrib import admin
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import NewUser              


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = NewUser
#     list_display = ("id","email","user_name","first_name", "is_staff", "is_active",)
#     list_filter = ("email","user_name","is_staff", "is_active",)
#     fieldsets = (
#         (None, {"fields": ("email",'user_name',"first_name")}),
#         ("Permissions", {"fields": ("is_staff", "is_active", )}),
#         ('Personal',{'fields':('about',)})
#     )
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": ('email','user_name','first_name','password1','password2','is_active')}
#         ),
#     )
#     search_fields=('email','user_name','first_name',)
    
#     ordering=('-start_date',)
# # admin.site.register(NewUser)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import NewUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = NewUser
    list_display = ("id","email","user_name","is_staff", "is_active",)
    list_filter = ("email","user_name", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email","user_name","first_name", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email","user_name","first_name")
    ordering = ('-start_date',)


admin.site.register(NewUser, CustomUserAdmin)