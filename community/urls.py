from django.urls import path, include
from .views import PostsListView, PostsDetailView, PostsCreateView, PostsDeleteView


app_name = 'community'

urlpatterns = [
    path('', PostsListView.as_view(), name='list'),
    path('detail/<int:pk>', PostsDetailView.as_view(), name='detail'),
    path('create', PostsCreateView.as_view(), name='create'),
    path('delete/<int:pk>', PostsDeleteView.as_view(), name='delete'),
]