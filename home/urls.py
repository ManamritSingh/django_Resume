from django.contrib import admin
from django.urls import path
from home import views
from .views import cv_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='Resume'),
    path('cv/', cv_view, name='cv')
]
