from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.BASE,name='base'),
    path('certificates',views.CERTIFICATE,name='base'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
