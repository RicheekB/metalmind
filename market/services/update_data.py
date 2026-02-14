import random
from datetime import date, timedelta
from decimal import Decimal
from django.utils import timezone
from market.models import Asset, PriceCandle, PriceSnapshot

def update_all_assets(days=5):
    """
    Ensures assets exist and generates mock data for the last 'days' days.
    """
    # Define assets to track
    assets_data = [
        {"slug": "gold", "name": "Gold", "symbol": "XAU", "base_price": 2300.00},
        {"slug": "silver", "name": "Silver", "symbol": "XAG", "base_price": 25.00},
        {"slug": "platinum", "name": "Platinum", "symbol": "XPT", "base_price": 950.00},
        {"slug": "palladium", "name": "Palladium", "symbol": "XPD", "base_price": 1000.00},
    ]

    summary = {}
    today = timezone.now().date()
    # Random seed removed to allow dynamic updates on each call

    for data in assets_data:
        asset, created = Asset.objects.get_or_create(
            slug=data["slug"],
            defaults={"name": data["name"], "symbol": data["symbol"]}
        )
        
        asset_summary = {"created": 0, "updated": 0, "snapshot_updated": False}
        base_price = data["base_price"]
        
        # Generate candles
        candles_created = 0
        candles_updated = 0
        
        # Keep track of the last price for snapshot
        last_price = Decimal(base_price)
        last_date = today

        for i in range(days):
            # Calculate date for the candle (going back 'days' from today)
            # If we want 5 days ending today: today-4, today-3, ..., today
            # Or ending yesterday? User said "writes/updates candles for last 5 days".
            # Let's assume ending today.
            candle_date = today - timedelta(days=(days - 1 - i))
            
            # Simple random walk: +/- 2%
            variation_pct = random.uniform(-0.02, 0.02)
            price_val = float(base_price) * (1 + variation_pct)
            price_decimal = Decimal(f"{price_val:.6f}")
            
            # Update base_price for next iteration (random walk)
            # base_price = price_val # Uncomment if we want random walk, but user said "small variations around a base price"
            # If we stick strictly to "variations around a base price", we keep base_price constant and just add noise.
            # "around a base price" usually implies mean reversion or noise, not necessarily a walk.
            # But "random seeded" suggests we want consistent output.
            # Let's do independent variation for now to keep it strictly "around base".
            
            obj, created_candle = PriceCandle.objects.update_or_create(
                asset=asset,
                date=candle_date,
                defaults={'close': price_decimal}
            )
            
            if created_candle:
                asset_summary["created"] += 1
            else:
                asset_summary["updated"] += 1
            
            last_price = price_decimal
            last_date = candle_date

        # Update Snapshot
        # Calculate change_pct (e.g., vs yesterday or just random)
        # Let's use the random variation from the base for now or 0 if single point.
        # Actually, let's use the difference from the previous candle if available, else 0.
        prev_date = last_date - timedelta(days=1)
        prev_candle = PriceCandle.objects.filter(asset=asset, date=prev_date).first()
        
        change_pct = Decimal(0)
        if prev_candle:
             change_pct = (last_price - prev_candle.close) / prev_candle.close * Decimal(100)
             
        # "as_of" needs to be datetime. specific time? Let's use now.
        PriceSnapshot.objects.update_or_create(
            asset=asset,
            defaults={
                'price': last_price,
                'change_pct': change_pct,
                'as_of': timezone.now()
            }
        )
        asset_summary["snapshot_updated"] = True
        
        summary[data["slug"]] = asset_summary

    return summary
