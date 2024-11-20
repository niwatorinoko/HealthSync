from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentications.urls')),  # `accounts/` のルート
    path('community/', include('community.urls')),  # `community/` のルート
    path('news/', include('news.urls')),  # `news/` のルート
    path('blog/', include('blog.urls')),  # `blog/` のルート
]

# Staticファイルのパターンを最後に定義
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
