
import logging
from typing import Optional, List, Dict, Any, Callable

_LOGGER = logging.getLogger(__name__)

class PriceAnalyzerLogic:
    """Class to handle the business logic for PriceAnalyzer."""

    def __init__(self, config: Dict[str, Any]):
        self._config = config
        self._percent_difference = config.get("percent_difference", 20)
        self._hours_to_boost = config.get("hours_to_boost", 2)
        self._hours_to_save = config.get("hours_to_save", 2)
        self._price_before_active = config.get("pa_price_before_active", 0.20)

    def is_gaining(self, current_hour_index: int, prices: List[float], threshold: float) -> bool:
        """Check if prices are gaining in the near future."""
        percent_threshold = (1 - float(threshold))
        
        if current_hour_index >= len(prices):
            return False
            
        price_now = prices[current_hour_index]
        if price_now is None:
            return False

        # Look ahead
        for i in reversed(range(self._hours_to_boost)):
            y = i + 1
            next_index = current_hour_index + y
            if next_index >= len(prices):
                continue
                
            price_next = prices[next_index]
            if price_next is None:
                continue
                
            price_next = max([price_next, 0.00001])
            if (price_now / price_next) < percent_threshold:
                return True
        return False

    def is_falling(self, current_hour_index: int, prices: List[float], threshold: float) -> bool:
        """Check if prices are falling in the near future."""
        percent_threshold = (1 + float(threshold))
        
        if current_hour_index >= len(prices):
            return False
            
        price_now = prices[current_hour_index]
        if price_now is None:
            return False

        # Look ahead
        for i in reversed(range(self._hours_to_save)):
            y = i + 1
            next_index = current_hour_index + y
            if next_index >= len(prices):
                continue
                
            price_next = prices[next_index]
            if price_next is None:
                continue
                
            price_next = max([price_next, 0.00001])
            if (price_now / price_next) > percent_threshold:
                return True
        return False

    def is_falling_alot_next_hour(self, item: Dict[str, Any]) -> bool:
        """Check if price is falling a lot in the next hour."""
        price_next = item.get('price_next_hour')
        value = item.get('value')
        
        if price_next is None or value is None:
            return False
            
        return (price_next / max([value, 0.00001])) < 0.60

    def calculate_temperature_correction(self, item: Dict[str, Any], day_stats: Dict[str, Any], 
                                       is_tomorrow: bool, reason: bool = False) -> Any:
        """Calculate the temperature correction based on price data."""
        is_gaining = item.get('is_gaining', False)
        is_falling = item.get('is_falling', False)
        is_max = item.get('is_max', False)
        is_low_price = item.get('is_low_price', False)
        is_five_most_expensive = item.get('is_five_most_expensive', False)
        
        # Extract stats
        diff = day_stats.get('diff', 0)
        max_price = day_stats.get('max', 0)
        
        percent_difference = (self._percent_difference + 100) / 100
        threshold = self._price_before_active
        
        below_threshold = float(threshold) > max_price
        if below_threshold:
            if reason:
                return 'Max-price below threshold'
            return 0

        if diff < percent_difference:
            if reason:
                return 'Small difference'
            return 0

        price_now = max([item.get("value", 0), 0.00001])
        price_next_hour = item.get("price_next_hour")
        if price_next_hour is None:
            price_next_hour = price_now
        price_next_hour = max([float(price_next_hour), 0.00001])

        is_pretty_cheap = price_now < 0.05
        
        # Special handling for high price at end of day
        # Note: item['start'] needs to be a datetime object or we need hour passed in
        # Assuming item['start'] is a datetime object as in original code
        hour = item.get('start').hour if hasattr(item.get('start'), 'hour') else 0
        
        if not is_tomorrow and hour == 23 and item.get('price_next_hour') is not None and \
           (price_next_hour / price_now) < 0.80 and not is_pretty_cheap:
            if reason:
                return 'Price dropping tomorrow'
            return -1
            
        if is_max:
            if reason:
                return 'Is max'
            return -1
        elif self.is_falling_alot_next_hour(item) and not is_pretty_cheap:
            if reason:
                return 'Is falling alot next hour'
            return -1
        elif is_gaining and (price_now < price_next_hour) and (not is_five_most_expensive):
            if reason:
                return 'Is gaining, and not in five most expensive hours'
            return 1
        elif is_falling and not is_low_price:
            if reason:
                return 'Is falling and not low price'
            return -1
        elif is_low_price and (not is_gaining or is_falling):
            if reason:
                return 'No need to correct.'
            return 0
        else:
            if reason:
                return 'No need to correct..'
            return 0
