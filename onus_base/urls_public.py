from django.conf.urls import include
from django.urls import path
from onus_base.views import HomeView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, loginPage, registerPage, logoutUser
from hospitals.views import DoctorView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerPage, name="register"),


    path('index_doctor/', DoctorView.as_view(), name='index_doctor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
