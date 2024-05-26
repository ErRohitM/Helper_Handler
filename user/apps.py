from django.apps import AppConfig
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

# accounts/apps.py



def create_custom_permissions(sender, **kwargs):
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType
    from .models import CustomUser

    content_type = ContentType.objects.get_for_model(CustomUser)

    permissions = [
        ("can_view_content", "Can view content"),
        ("can_edit_content", "Can edit content"),
    ]

    for codename, name in permissions:
        Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        post_migrate.connect(create_custom_permissions, sender=self)

