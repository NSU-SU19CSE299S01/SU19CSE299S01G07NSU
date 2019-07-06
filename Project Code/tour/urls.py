from django.conf.urls import url
from tour import views
app_name = 'tour'
urlpatterns =[
    url(r'^sylhet/$',views.sylhet,name='sylhet'),

]