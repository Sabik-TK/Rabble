from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('social/', include('social_django.urls', namespace='social')),
    path('api-auth/', include('rest_framework.urls',)),
    path('admin/', admin.site.urls),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api/',include('apps.api.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

