from django.contrib import admin
from django.urls import include, path
from banks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include('banks.urls')),

]
