from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('operational research', views.op, name='op'),
    path("Simplex Method", views.sim, name="sim" )
]
