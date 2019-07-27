from django.urls import path
from django.conf.urls import url
from community import views

urlpatterns = [
    url(r'^PostList/$', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]