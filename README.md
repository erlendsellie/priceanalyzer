# PriceAnalyzer - Smart Energy Management for Home Assistant

An intelligent Home Assistant integration that optimizes your energy consumption based on Nordpool electricity prices. Automatically control thermostats and hot water heaters to minimize costs while maintaining comfort.

Originally based on the excellent [nordpool custom component](https://github.com/custom-components/nordpool).

![PriceAnalyzer Screenshot](https://user-images.githubusercontent.com/18458417/197388506-d623cb01-141d-4e44-b384-5a3aa21975a0.png)

## What does it do?

PriceAnalyzer analyzes hourly (or 15-minute) electricity prices from Nordpool and provides smart sensors that help you:
- **Save money** by shifting energy consumption to cheaper hours
- **Optimize comfort** by preheating during low-price periods
- **Reduce environmental impact** by using electricity when it's greenest (often correlates with price)

### Support the Project

If you find this useful:
- [Buy me a beer](http://paypal.me/erlendsellie) or a [Ko-fi](https://ko-fi.com/erlendsellie)
- Support on [Patreon](https://www.patreon.com/erlendsellie) [![Patreon](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/erlendsellie)
- Get [50 EUR off Tibber smart home gadgets](https://invite.tibber.com/yuxfw0uu) (referral link)
- Thinking about a Tesla? Get discounts using my [referral link](https://ts.la/erlend56568)

---

## Features

### 🌡️ Climate Control Sensor (PriceAnalyzerSensor)
Provides intelligent temperature correction recommendations (±1°C) for your thermostats based on current and upcoming electricity prices.

**How it works:**
- **Pre-heating**: Increases temperature when prices are about to rise
- **Energy saving**: Reduces temperature during price peaks or when prices are falling
- **Smart timing**: Looks ahead at the next few hours to optimize comfort and cost

**Sensor attributes include:**
- `is_ten_cheapest` / `is_five_cheapest` / `is_two_cheapest` - Boolean flags for cheapest hours
- `ten_cheapest_today` / `five_cheapest_today` / `two_cheapest_today` - Lists of cheapest hours
- `is_gaining` / `is_falling` - Price trend indicators
- `is_over_peak` / `is_over_average` - Price level indicators
- `temperature_correction` - Recommended adjustment for your thermostat
- Full price data for today and tomorrow

### 💧 Hot Water Heater Sensor (VVBSensor)
Calculates optimal water heater temperatures based on electricity prices to ensure you always have hot water while minimizing costs.

**Default temperature strategy:**
- **75°C** - Default and minimum price hours (always hot water)
- **70°C** - Five cheapest hours
- **65°C** - Ten cheapest hours  
- **60°C** - Low price hours
- **50°C** - Normal hours and falling prices
- **40°C** - Five most expensive hours (minimum safe temperature)

You can customize all these temperatures in the integration settings to match your hot water heater capacity, insulation, and household usage patterns.

**Binary mode:** Can also be configured as simple ON/OFF if you don't have temperature control.

### 💰 Price Sensor (PriceSensor)
Displays the current electricity price with your configured additional costs (grid fees, taxes, etc.) applied.

---

## Installation

### Via HACS (Recommended)

1. Open HACS in your Home Assistant
2. Click the three dots (⋮) in the top right corner
3. Select **Custom repositories**
4. Add this repository URL: `https://github.com/erlendsellie/priceanalyzer/`
5. Select **Integration** as the category
6. Click **Add**
7. Search for "PriceAnalyzer" and click **Download**
8. **Restart Home Assistant**
9. Go to **Settings** → **Devices & Services** → **Add Integration** → Search for "PriceAnalyzer"

### Manual Installation

1. Copy the `custom_components/priceanalyzer` folder to your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant
3. Go to **Settings** → **Devices & Services** → **Add Integration** → Search for "PriceAnalyzer"

---

## Configuration

### Basic Setup

When adding the integration through the UI, you'll configure:

**Step 1: Basic Settings**
- **Friendly name** (optional): Custom name to distinguish multiple setups
- **Region**: Your Nordpool price area (e.g., NO1, NO2, SE3, DK1, etc.)
- **Currency**: Your preferred currency (auto-detected based on region)
- **Include VAT**: Whether to include VAT in prices
- **Time resolution**: 
  - `hourly` - Standard hourly prices (default)
  - `quarterly` - 15-minute price intervals (for compatible regions)

**Step 2: Price Settings**
- **Price type**: Display as kWh, MWh, or Wh
- **Show in cents**: Display prices in cents/øre instead of currency
- **Low price cutoff**: Multiplier for determining "low price" (default: 1.0 = average price)
- **Additional costs template**: Jinja2 template for grid fees, taxes, etc.
  - Example: `{{0.50|float}}` adds 0.50 to the price
  - Example: `{{current_price * 0.25}}` adds 25% markup

**Step 3: Advanced Settings**
- **Multiply template**: Adjustment factor for temperature correction
- **Hours to boost/save**: Look-ahead window for price trends
- **Percent difference**: Minimum price variation threshold
- **Price before active**: Minimum price to activate features

**Step 4: Hot Water Temperature Settings**
Configure target temperatures for different price scenarios:
- **Default temperature**: Normal operating temperature (default: 75°C)
- **Five most expensive hours**: Minimum temperature during peaks (default: 40°C)
- **Price falling**: Temperature when price is declining (default: 50°C)
- **Five cheapest hours**: Maximum temperature for cheap hours (default: 70°C)
- **Ten cheapest hours**: Temperature for top 10 cheap hours (default: 65°C)
- **Low price hours**: Temperature below average price (default: 60°C)
- **Normal hours**: Temperature for average prices (default: 50°C)
- **Minimum price**: Temperature at lowest daily price (default: 75°C)

**For binary control:** Use values like `1.0` (ON) and `0.0` (OFF) instead of temperatures.

### Multiple Setups

You can create multiple PriceAnalyzer integrations for the same region with different configurations. This is useful for:
- Different additional costs calculations
- Separate hot water heater configurations
- Testing different strategies
- Multiple households/installations

Each setup is identified by its friendly name and creates its own set of sensors.

### Reconfiguring

To change settings after initial setup:
1. Go to **Settings** → **Devices & Services**
2. Find your PriceAnalyzer integration
3. Click **Configure**
4. Make your changes in the multi-step menu

---

## Usage

### Automating Climate Control

Use PriceAnalyzer to automatically adjust your thermostat based on electricity prices:

**Step 1:** Create an Input Number helper to store your base temperature
- Click here to create: [![Create Input Helper](https://my.home-assistant.io/badges/helpers.svg)](https://my.home-assistant.io/redirect/helpers/)
- Name it something like "Living Room Base Temperature"
- Set min/max values appropriate for your climate (e.g., 18-24°C)

**Step 2:** Import the Climate Control Blueprint
- Click here: [![Import Climate Control Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Ferlendsellie%2Fpriceanalyzer%2Fblob%2Fmaster%2Fblueprints%2Fautomation%2Fpriceanalyzer%2Fpriceanalyzer.yaml)
- Select your input number, PriceAnalyzer sensor, and climate entity
- The automation will adjust your thermostat by ±1°C based on price trends

**How it works:**
- When prices are about to rise → Pre-heats your home
- During price peaks → Reduces temperature slightly  
- When prices are falling → Lowers temperature to save energy
- Your base temperature remains in your input number for manual control

### Automating Hot Water Heater

Use PriceAnalyzer to optimize hot water heating costs:

**Import the Hot Water Blueprint:**
[![Import Hot Water Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Ferlendsellie%2Fpriceanalyzer%2Fblob%2Fmaster%2Fblueprints%2Fautomation%2Fpriceanalyzer%2Fpriceanalyzer_vvb.yaml)

- Select your VVBSensor and hot water heater thermostat/switch
- The automation sets the appropriate temperature based on current price conditions
- Ensures hot water availability while minimizing heating costs

### Advanced Usage

**Using cheapest hours attributes in automations:**
```yaml
# Example: Run dishwasher during cheapest hours
automation:
  - trigger:
      - platform: template
        value_template: >
          {{ state_attr('sensor.priceanalyzer_no3', 'current_hour')['is_two_cheapest'] }}
    action:
      - service: switch.turn_on
        target:
          entity_id: switch.dishwasher
```

**Custom templates with additional costs:**
The additional costs template receives `current_price` as a variable:
```jinja
# Add fixed grid fee + 25% tax
{{ (current_price + 0.50) * 1.25 }}

# Time-based additional costs
{% if now().hour >= 6 and now().hour < 22 %}
  {{ current_price + 0.40 }}  {# Day tariff #}
{% else %}
  {{ current_price + 0.20 }}  {# Night tariff #}
{% endif %}
```

---

## Troubleshooting

### Enable Debug Logging

If you're experiencing issues, enable debug logging to see detailed information:

**Via UI (Recommended):**
1. Go to **Settings** → **System** → **Logs**
2. Click **Configure** for `custom_components.priceanalyzer`
3. Set level to **Debug**

**Via configuration.yaml:**
```yaml
logger:
  default: info
  logs:
    custom_components.priceanalyzer: debug
    nordpool: debug  # For API communication issues
```

### Getting Help

- **Wiki**: https://github.com/erlendsellie/priceanalyzer/wiki
- **Issues**: https://github.com/erlendsellie/priceanalyzer/issues
- **Discussions**: Use GitHub Discussions for questions

---

## Credits

Originally based on the excellent [nordpool](https://github.com/custom-components/nordpool) custom component.

## License

MIT License - See LICENSE file for details
