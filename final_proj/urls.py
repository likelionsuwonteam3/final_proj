from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('blog/<int:blog_id>/',views.more, name='more')
]
