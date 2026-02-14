from django.core.management.base import BaseCommand
from market.services.update_data import update_all_assets

class Command(BaseCommand):
    help = 'Updates asset prices with mock data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=5,
            help='Number of days of data to generate',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing price data before updating',
        )

    def handle(self, *args, **options):
        days = options['days']
        clear = options['clear']
        
        if clear:
            self.stdout.write("Clearing all existing price data...")
            from market.models import PriceCandle, PriceSnapshot
            PriceCandle.objects.all().delete()
            PriceSnapshot.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Data cleared."))

        self.stdout.write(f"Updating asset prices for the last {days} days...")
        
        summary = update_all_assets(days=days)
        
        for asset_slug, stats in summary.items():
            self.stdout.write(
                self.style.SUCCESS(
                    f"Asset '{asset_slug}': Created {stats['created']} candles, "
                    f"Updated {stats['updated']} candles. Snapshot updated."
                )
            )
