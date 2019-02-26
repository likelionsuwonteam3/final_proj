from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('detail/', views.detail, name='detail'),
    path('<int:blog_id>/',views.more, name='more'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

]
