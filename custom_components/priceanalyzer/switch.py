import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import SWITCH_NAME, SWITCH_DEFAULT_STATE, SWITCH_DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType = None,
) -> None:
    """Set up the PriceAnalyzer switch platform."""
    async_add_entities([PriceAnalyzerSwitch(hass)], True)

class PriceAnalyzerSwitch(SwitchEntity):
    """Representation of a PriceAnalyzer switch."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the switch."""
        self._hass = hass
        self._name = SWITCH_NAME
        self._state = SWITCH_DEFAULT_STATE

    @property
    def name(self) -> str:
        """Return the name of the switch."""
        return self._name

    @property
    def is_on(self) -> bool:
        """Return true if the switch is on."""
        return self._state

    async def async_turn_on(self, **kwargs) -> None:
        """Turn the switch on."""
        self._state = True
        self._hass.states.async_set(f"{SWITCH_DOMAIN}.{self._name}", self._state)
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs) -> None:
        """Turn the switch off."""
        self._state = False
        self._hass.states.async_set(f"{SWITCH_DOMAIN}.{self._name}", self._state)
        self.async_write_ha_state()

    async def async_update(self) -> None:
        """Fetch new state data for the switch."""
        state = self._hass.states.get(f"{SWITCH_DOMAIN}.{self._name}")
        if state:
            self._state = state.state == "on"
