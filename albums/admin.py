from django.contrib import admin
from .models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'description', 'owner__username')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'uploaded_by', 'created_at')
    search_fields = ('title', 'caption', 'album__title')
