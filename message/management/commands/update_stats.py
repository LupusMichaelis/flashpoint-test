from django.core.management.base import BaseCommand, CommandError
from message.models import Messages, Stats
from django.db.models import Count

class Command(BaseCommand):
    help = 'Update message stats'

    def handle(self, *args, **options):
        stats = Messages.objects.aggregate(users=Count('username', distinct=True),
                cities=Count('city', distinct=True))
        stats, created = Stats.objects.update_or_create(defaults=stats)
        stats.save()
