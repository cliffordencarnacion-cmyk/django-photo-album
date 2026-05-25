from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

User = get_user_model()


class Album(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_photo_count(self):
        return self.photos.count()


class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    caption = models.TextField(blank=True)
    image = CloudinaryField('image')
    uploaded_by = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
