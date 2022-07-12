from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from phonenumber_field.phonenumber import PhoneNumber, to_python


def validate_international_phonenumber(value):
    phone_number = to_python(value)
    if isinstance(phone_number, PhoneNumber) and not phone_number.is_valid():
        raise ValidationError(
            _("The phone number entered is not valid."), code="invalid_phone_number"
        )
        
def user_exists(username):
    if User.objects.filter(username= username):
        return True
    return False
  
def check_sympols(input):
    """ 
    Some fields cannot contain symplos, This method check if the input contain any sympols.
    """

    sympols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '<',
               '>', ',', '.', '?', '/', '\\', '|', '[', ']', '{', '}', ';', "'", '"', ':', '_']
   # Loop within input range
    
    for i,char in enumerate(input):
        # Iterate over sympols
    
        for sympol in sympols:
            # Check if char in input equals the iterated sympol rais a VError.
            
            if input[i] == sympol:
                
                raise ValidationError(
                    _(f'input cannot contain sympols! Please enter another input'))