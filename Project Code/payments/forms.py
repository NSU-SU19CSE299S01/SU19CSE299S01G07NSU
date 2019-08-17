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

class CrispyAddressForm(AddressForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('Amount', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('TrxID', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Donate')
        )

class CustomCheckbox(Field):
    template = 'custom_checkbox.html'


class CustomFieldForm(AddressForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('Amount', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('TrxID', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            CustomCheckbox('check_me_out'),
            Submit('submit', 'Donate')
        )
