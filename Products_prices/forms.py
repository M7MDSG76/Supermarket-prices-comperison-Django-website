from django import forms
import datetime
from django.core.exceptions import ValidationError 
from django.utils.translation import gettext_lazy as _



from .models import *


class NewItemForm(forms.ModelForm):
    """
    To do it tomorrow!...
    """
    class Meta:
        model = Item
        fields = ['product', 'supermarket_branch', 'price']
    pass