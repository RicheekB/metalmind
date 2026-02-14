from decimal import Decimal
from typing import List
import statistics

# Constants for trend and volatility thresholds
TREND_THRESHOLD_PCT = Decimal("0.3")
VOLATILITY_LOW_THRESHOLD = 0.4
VOLATILITY_HIGH_THRESHOLD = 1.0

def calculate_trend(last_5_closes: List[Decimal]) -> str:
    """
    Calculates the price trend based on the percent change between the first and last close.
    Returns: "Up", "Down", or "Sideways"
    """
    if len(last_5_closes) < 2:
        return "Sideways"
        
    first = last_5_closes[0]
    last = last_5_closes[-1]
    
    if first == 0:
        return "Sideways"
        
    change_pct = (last - first) / first * Decimal(100)
    
    if change_pct > TREND_THRESHOLD_PCT:
        return "Up"
    elif change_pct < -TREND_THRESHOLD_PCT:
        return "Down"
    return "Sideways"

def calculate_volatility(last_5_closes: List[Decimal]) -> str:
    """
    Calculates volatility based on the standard deviation of daily percent changes.
    Returns: "Low", "Medium", or "High"
    """
    if len(last_5_closes) < 2:
        return "Low"
        
    pct_changes = []
    
    # Calculate percentage changes between consecutive days
    for i in range(1, len(last_5_closes)):
        prev = last_5_closes[i-1]
        cur = last_5_closes[i]
        
        if prev == 0:
            pct = 0.0
        else:
            pct = float((cur - prev) / prev * Decimal(100))
        pct_changes.append(pct)
        
    # Standard deviation of percent changes
    std = statistics.pstdev(pct_changes) if pct_changes else 0.0
    
    if std < VOLATILITY_LOW_THRESHOLD:
        return "Low"
    elif std <= VOLATILITY_HIGH_THRESHOLD:
        return "Medium"
    else:
        return "High"
