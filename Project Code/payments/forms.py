from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field


STATES = (
    ('', 'Choose...'),
    ('DHK', 'Dhaka'),
    ('SYL', 'Sylhet'),
    ('RAJ', 'Rajshahi'),
    ('BAR', 'Barisal'),
    ('KHU', 'Khulna'),
    ('CTG', 'Chittagong'),
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    Amount = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    TrxID = forms.CharField(label='BKash-01920101801',widget=forms.TextInput(attrs={'placeholder': 'TrxID'}))
    check_me_out = forms.BooleanField(required=False)

