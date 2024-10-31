from django.contrib import admin
from django.urls import path, include
from .views import PostsListView


app_name = 'community'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostsListView.as_view(), name='list'),
    # path('diary/detail/<int:pk>', DiaryDetailView.as_view(), name='detail'),
    # path('diary/create/', DiaryCreateView.as_view(), name='create'),
    # path('diary/delete/<int:pk>', DiaryDeleteView.as_view(), name='delete'),
]