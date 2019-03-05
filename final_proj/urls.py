from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/detail/', views.detail, name='detail'),
    path('blog/<int:blog_id>/',views.more, name='more'),
    path('blog/new/', views.new, name='new'),
    path('blog/create/', views.create, name='create'),
    path('blog/portfolio/',views.portfolio, name='portfolio'),
    path('blog/create_port/', views.create_port, name='create_port'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
