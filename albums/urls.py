from django.urls import path
from .views import (
    AlbumListView,
    AlbumDetailView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
)

urlpatterns = [
    path('', AlbumListView.as_view(), name='album-list'),
    path('albums/add/', AlbumCreateView.as_view(), name='album-add'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('albums/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album-edit'),
    path('albums/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
    path('albums/<int:album_pk>/photos/add/', PhotoCreateView.as_view(), name='photo-add'),
    path('photos/<int:pk>/edit/', PhotoUpdateView.as_view(), name='photo-edit'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
]
