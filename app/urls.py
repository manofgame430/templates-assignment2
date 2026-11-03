from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', home_view),
    path('<team>/', team_view, name='team'),
]