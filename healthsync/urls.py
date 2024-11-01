from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('authentications.urls')),  # `accounts/` のルート
    path('community/', include('community.urls')),  # `community/` のルート
]

# Staticファイルのパターンを最後に定義
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
