from django.urls import path as url
from django.conf.urls import include
from . import views

urlpatterns = [
    url('app/',views.index),
    url('execute/',views.execute),
    url('compilersopts/',views.compilersoption),
    ]
