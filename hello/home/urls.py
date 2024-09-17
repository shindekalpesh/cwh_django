from django.contrib import admin
from django.urls import path, include
from home import views

# To change admin portal display text
admin.site.site_header = "CWH Icecream Admin"
admin.site.site_title = "CWH Icecream Admin Portal"
admin.site.index_title = "Welcome to CWH Icecream"

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]