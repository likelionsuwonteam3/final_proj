from django.contrib import admin
from django.urls import path,include
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/',include('main.urls')),

]
