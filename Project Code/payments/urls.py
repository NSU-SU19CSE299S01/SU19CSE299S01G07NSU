from django.conf.urls import url
from payments import views


urlpatterns = [
    url(r'^form_3/$', views.AddressFormView.as_view(template_name='payments/form_3.html'), name='form_3'),
    url(r'^form_4/$', views.CrispyAddressFormView.as_view(), name='form_4'),
    url(r'^form_5/$', views.CustomFieldFormView.as_view(), name='form_5'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),
    url(r'^charge/$', views.charge, name='charge'),
]