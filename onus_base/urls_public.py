from django.conf.urls import include
from django.urls import path
from onus_base.views import HomeView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view()),
    # path('admin/', admin.site.urls),
    path('index_doctor/', DoctorView.as_view(), name='index_doctor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
