from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Create the Album Administrator role for RBAC enforcement.'

    def handle(self, *args, **options):
        from albums.models import Album, Photo

        group, created = Group.objects.get_or_create(name='Album Administrator')
        album_type = ContentType.objects.get_for_model(Album)
        photo_type = ContentType.objects.get_for_model(Photo)

        permissions = Permission.objects.filter(
            content_type__in=[album_type, photo_type],
            codename__in=[
                'add_album', 'change_album', 'delete_album',
                'add_photo', 'change_photo', 'delete_photo',
            ],
        )
        group.permissions.set(permissions)

        if created:
            self.stdout.write(self.style.SUCCESS('Created the Album Administrator group and assigned permissions.'))
        else:
            self.stdout.write(self.style.SUCCESS('Album Administrator group exists and permissions were updated.'))
