from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('admin/', admin.site.urls)
]