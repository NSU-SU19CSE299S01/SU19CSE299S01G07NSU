from django.conf.urls import url
from tour import views
app_name = 'tour'
urlpatterns =[
    url(r'^sylhet/$',views.sylhet,name='sylhet'),
    url(r'^barisal/$',views.barisal,name='barisal'),
    url(r'^rajshahi/$',views.rajshahi,name='rajshahi'),
    url(r'^saint_martin/$',views.saint_martin,name='saint_martin'),
    url(r'^khulna/$',views.khulna,name='khulna'),
    url(r'^chittagong/$',views.chittagong,name='chittagong'),
    url(r'^dhaka/$',views.dhaka,name='dhaka'),

    url(r'^syl/$',views.syl,name='syl'),
    url(r'^khu/$',views.khu,name='khu'),
    url(r'^bar/$',views.bar,name='bar'),
    url(r'^raj/$',views.raj,name='raj'),
    url(r'^dhk/$',views.dhk,name='dhk'),
    url(r'^ctg/$',views.ctg,name='ctg'),
    url(r'^map/$',views.map,name='map'),
    url(r'^hotel/$',views.hotel,name='hotel'),


]