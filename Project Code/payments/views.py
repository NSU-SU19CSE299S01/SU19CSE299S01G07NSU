from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.conf import settings
from .forms import AddressForm, CrispyAddressForm, CustomFieldForm
import stripe
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY

class AddressFormView(FormView):
    form_class = AddressForm
    success_url = reverse_lazy('success')


    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


class CrispyAddressFormView(FormView):
    form_class = CrispyAddressForm
    success_url = reverse_lazy('success')
    template_name = 'payments/crispy_form.html'

