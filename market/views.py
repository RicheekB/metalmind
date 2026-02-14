from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from .models import Asset, PriceCandle, PriceSnapshot
from .services.metrics import calculate_trend, calculate_volatility
from .services.update_data import update_all_assets
from datetime import timedelta, date
from decimal import Decimal

# Dashboard (requires login)
@login_required
def dashboard(request):
    assets = Asset.objects.all()
    snapshots = {a.slug: PriceSnapshot.objects.filter(asset=a).order_by('-as_of').first() for a in assets}
    return render(request, 'market/dashboard.html', {'assets': assets, 'snapshots': snapshots})

@login_required
def asset_detail(request, slug):
    asset = get_object_or_404(Asset, slug=slug)
    days = int(request.GET.get('days', 5))
    end = date.today()
    start = end - timedelta(days=days-1)
    candles = list(PriceCandle.objects.filter(asset=asset, date__range=(start, end)).order_by('date'))
    closes = [c.close for c in candles]
    trend = calculate_trend(closes)
    volatility = calculate_volatility(closes)
    snapshot = PriceSnapshot.objects.filter(asset=asset).order_by('-as_of').first()
    # prepare JSON data for Chart.js
    chart_data = {
        'labels': [c.date.isoformat() for c in candles],
        'closes': [str(c.close) for c in candles],
    }
    return render(request, 'market/asset_detail.html', {
        'asset': asset, 'candles': candles, 'closes': closes,
        'trend': trend, 'volatility': volatility, 'snapshot': snapshot,
        'chart_data': chart_data
    })

# API JSON endpoints (no auth needed for demo)
def api_assets(request):
    assets = Asset.objects.all()
    data = []
    for a in assets:
        snap = PriceSnapshot.objects.filter(asset=a).order_by('-as_of').first()
        data.append({
            'slug': a.slug,
            'name': a.name,
            'symbol': a.symbol,
            'latest_price': str(snap.price) if snap else None,
            'change_pct': str(snap.change_pct) if snap else None,
            'as_of': snap.as_of.isoformat() if snap else None,
        })
    return JsonResponse({'assets': data})

def api_candles(request, slug):
    days = int(request.GET.get('days', 5))
    asset = get_object_or_404(Asset, slug=slug)
    end = date.today()
    start = end - timedelta(days=days-1)
    candles = PriceCandle.objects.filter(asset=asset, date__range=(start, end)).order_by('date')
    data = [{'date': c.date.isoformat(), 'close': str(c.close)} for c in candles]
    return JsonResponse({'asset': slug, 'candles': data})

# Manual update endpoint (POST, login required)
@login_required
def api_update(request):
    if request.method != 'POST':
        return HttpResponseForbidden('POST required')
    summary = update_all_assets(days=5)
    # redirect back to dashboard
    return redirect('dashboard')
