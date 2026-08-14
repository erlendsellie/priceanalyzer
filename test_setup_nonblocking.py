from pathlib import Path


ROOT = Path(__file__).parent / "custom_components" / "priceanalyzer"


def test_setup_does_not_wait_for_price_downloads():
    sensor_source = (ROOT / "sensor.py").read_text()
    integration_source = (ROOT / "__init__.py").read_text()

    assert "await self._data.check_stuff()" not in sensor_source
    assert "entry.async_create_background_task(" in integration_source


if __name__ == "__main__":
    test_setup_does_not_wait_for_price_downloads()
