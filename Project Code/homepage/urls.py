from django.conf.urls import url
from homepage import views

app_name = "homepage"
urlpatterns =[
    url(r'^$',views.index,name='index')

]