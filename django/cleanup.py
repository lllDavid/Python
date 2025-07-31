# myapp/management/commands/cleanup_inactive_users.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from myapp.models import UserProfile  

class Command(BaseCommand):
    help = 'Delete user profiles inactive for over a year'

    def handle(self, *args, **options):
        cutoff_date = timezone.now() - timedelta(days=365)
        inactive_users = UserProfile.objects.filter(last_active__lt=cutoff_date)

        count = inactive_users.count()
        inactive_users.delete()
        self.stdout.write(f'Deleted {count} inactive user profiles.')