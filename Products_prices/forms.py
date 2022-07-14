import datetime
from enum import unique

from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

from .models import *
from .my_validators import validate_international_phonenumber, check_sympols

from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError 
from django.contrib.auth import authenticate


class NewItemForm(forms.ModelForm):
    """
         ________
    Done |    /  |
         |  \/   |
         ---------
    """
    class Meta:
        model = Item
        fields = ['product', 'supermarket_branch', 'price']
    pass






username_validator = UnicodeUsernameValidator()
EmailValidator = EmailValidator()

class CreateConsumerForm(forms.Form):
    """
    Consumer class is to give our user the ability to contribute with the grocery products prices follow-up,
    and more feutres in the future.
    
    Consumer class will be related with the built-in User class for the authintecation perpuses,
    therefore the next is required:
        - username.
        - password.
        
    Consumer Fields are:
        1- username (Required).
        2- password (Required).
        3- first name.
        4- seconde name.
        5- last name.
        6- email.
        7- phone number.
    """
    username = forms.CharField(label= _("username"), max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },)
    password = forms.CharField(label= _("password"), max_length=128)
    first_name = forms.CharField(label= _("first name"), max_length=150)
    last_name = forms.CharField(label= _("last name"), max_length=150)
    email = forms.EmailField(label= _("email address"),validators=[EmailValidator])
    phone_no = forms.CharField(label= _('Phone Number'))
    
    def clean_username(self):
        data = self.cleaned_data['username']
        
      
        if User.objects.filter(username=data).exists():
            raise ValidationError(_('Username is already used'))
        return data


    def clean_password(self):
        data = self.cleaned_data['password']
        return data


    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        
        check_sympols(data)
            
        return data


    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        
        check_sympols(data)
        
        return data


    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError(_('Email is already used'))
        return data

    def clean_phone_no(self):
        data = self.cleaned_data['phone_no']
        if Consumer.objects.filter(phone_no=data).exists():
            raise ValidationError(_('Phone number is already used'))
        validate_international_phonenumber(data)
        
        return data


class LoginUserForm(forms.Form):
    username = forms.CharField(label= _("username"), max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },)
    password = forms.CharField(label= _("password"), max_length=128)
    
    def clean_username(self):
        data = self.cleaned_data['username']
        return data


    def clean_password(self):
        data = self.cleaned_data['password']
        return data

    