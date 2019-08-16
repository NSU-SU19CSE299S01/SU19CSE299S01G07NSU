from django.urls import path
from django.conf.urls import url
from community import views

urlpatterns = [
    url(r'^PostList/$', views.PostList.as_view(), name='home'),
    url(r'^post_new/$', views.post_new, name='post_new'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]