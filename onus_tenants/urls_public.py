from django.conf.urls import include
from django.urls import path
from onus_tenants.views import HomeView
from django.contrib import admin

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
]
