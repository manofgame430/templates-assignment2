from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', home_view),
    path('<str:team>/', team_view, name="Leadership_team"),
]