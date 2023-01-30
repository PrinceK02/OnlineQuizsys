from django.urls import path as url
from django.conf.urls import include
from django.views.generic import ListView, DetailView
from theory.models import Quest
from . import views
from theory.views import *
#from theory.views import details
import re
from django.db import models
urlpatterns = [
    url('',views.index),
    #path("theory/<int:id>/", views.details),
    ]
