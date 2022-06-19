from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin





urlpatterns = [
    path('',views.home,name="home"),
    path('dengue',views.dengue,name="dengue"),
    path('dengue_test',views.dengue_test,name="dengue_test"),


    
    
]