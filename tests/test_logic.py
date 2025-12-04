
import unittest
from datetime import datetime
from custom_components.priceanalyzer.logic import PriceAnalyzerLogic

class TestPriceAnalyzerLogic(unittest.TestCase):
    def setUp(self):
        self.config = {
            "percent_difference": 20,
            "hours_to_boost": 2,
            "hours_to_save": 2,
            "pa_price_before_active": 0.20
        }
        self.logic = PriceAnalyzerLogic(self.config)

    def test_is_gaining(self):
        # Test gaining prices
        prices = [1.0, 1.5, 2.0, 1.0]
        # Threshold 0.2 means percent_threshold is 0.8
        # 1.0 / 1.5 = 0.66 < 0.8 -> True
        self.assertTrue(self.logic.is_gaining(0, prices, 0.2))
        
        # Test not gaining
        prices = [1.0, 0.9, 0.8, 1.0]
        self.assertFalse(self.logic.is_gaining(0, prices, 0.2))

    def test_is_falling(self):
        # Test falling prices
        prices = [2.0, 1.0, 0.5, 2.0]
        # Threshold 0.2 means percent_threshold is 1.2
        # 2.0 / 1.0 = 2.0 > 1.2 -> True
        self.assertTrue(self.logic.is_falling(0, prices, 0.2))
        
        # Test not falling
        prices = [1.0, 1.1, 1.2, 1.0]
        self.assertFalse(self.logic.is_falling(0, prices, 0.2))

    def test_calculate_temperature_correction_small_diff(self):
        item = {
            'value': 1.0,
            'price_next_hour': 1.0,
            'is_gaining': False,
            'is_falling': False,
            'is_max': False,
            'is_low_price': False,
            'start': datetime(2023, 1, 1, 12, 0, 0)
        }
        day_stats = {
            'diff': 1.1, # Small difference (less than 1.2)
            'max': 1.5
        }
        
        result = self.logic.calculate_temperature_correction(item, day_stats, False)
        self.assertEqual(result, 0)
        
        reason = self.logic.calculate_temperature_correction(item, day_stats, False, True)
        self.assertEqual(reason, 'Small difference')

    def test_calculate_temperature_correction_max(self):
        item = {
            'value': 2.0,
            'price_next_hour': 1.0,
            'is_gaining': False,
            'is_falling': False,
            'is_max': True,
            'is_low_price': False,
            'start': datetime(2023, 1, 1, 12, 0, 0)
        }
        day_stats = {
            'diff': 2.0,
            'max': 2.0
        }
        
        result = self.logic.calculate_temperature_correction(item, day_stats, False)
        self.assertEqual(result, -1)
        
        reason = self.logic.calculate_temperature_correction(item, day_stats, False, True)
        self.assertEqual(reason, 'Is max')

if __name__ == '__main__':
    unittest.main()
