from django import forms
from .models import Customer, ContactPerson

# Form for Customer model
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['business_name', 'p_iva', 'sdi_code', 'pec', 'email', 'phone', 'address']

# Form for ContactPerson model
class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = ['first_name', 'last_name', 'cell', 'email', 'role', 'customer']

