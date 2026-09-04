# Data Dictionary

The dataset contains simulated environmental observations for four plant profiles.

| Variable | Description | Unit / Range | Source |
|---|---|---|---|
| `plant_id` | Identifier for the monitored plant profile | Text | Python plant profile |
| `temp` | Environmental temperature | °C | DHT22 in Wokwi simulation |
| `humidity` | Relative humidity | % | DHT22 in Wokwi simulation |
| `soil` | Relative soil-moisture level | 0–100 % | Potentiometer in Wokwi simulation |

## Important notes

- The current dataset is **simulated**, not collected from physical plants.
- Soil moisture is a relative percentage generated from the Wokwi potentiometer. It is **not calibrated volumetric water content**.
- The plant ranges used by the Python program are simple rule-based thresholds for this learning project; they should not be treated as precise horticultural recommendations.
- Blank lines in the original dataset were removed so the CSV can be read consistently as a table.
