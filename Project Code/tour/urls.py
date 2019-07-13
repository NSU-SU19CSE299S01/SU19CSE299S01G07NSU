from django.conf.urls import url
from tour import views
app_name = 'tour'
urlpatterns =[
    url(r'^sylhet/$',views.sylhet,name='sylhet'),
    url(r'^barisal/$',views.barisal,name='barisal'),
    url(r'^rajshahi/$',views.rajshahi,name='rajshahi'),

]