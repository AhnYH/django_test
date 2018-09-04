from django.urls import path
from django.conf.urls import url
from . import views as views

urlpatterns = [
    url('signin$', views.signin),
    url('login$', views.login),
    url('api/v1/coSpaces$', views.req_test),
    url('api/v1/coSpaces/(?P<id>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})$', views.req_detail),
]