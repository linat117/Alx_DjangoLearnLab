from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(actor, recipient, verb, target=None):
    Notification.objects.create(
        actor=actor,
        recipient=recipient,
        verb=verb,
        target_content_type=ContentType.objects.get_for_model(target) if target else None,
        target_object_id=target.id if target else None
    )
