from django.urls import path
from django.conf.urls import url
from . import views as views

urlpatterns = [
    url('signin$', views.signin),
    url('login$', views.login),
    url('api/v1/coSpaces$', views.req_test),
]