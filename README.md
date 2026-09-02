# Eco-pro 🌱

### A low-cost environmental sensing and decision-support experiment

Eco-pro is an evolving environmental sensing project exploring how
low-cost sensors, Python, and data analysis can be combined to monitor
and interpret changing environmental conditions.

The project currently uses a simulated Arduino-based sensing system to
collect:

- Temperature
- Relative humidity
- Soil moisture

The sensor readings are processed using Python and used to generate
simple plant-specific recommendations.

The long-term goal is to explore how environmental sensing and
computational methods can support more informed environmental
decision-making.

---

## 🔬 Research Question

**How can low-cost environmental sensors and simple computational
methods be used to monitor changing micro-environmental conditions
and translate sensor measurements into useful decisions?**

---

## 🎯 Current Objectives

1. Collect environmental measurements using Arduino-based sensors.
2. Simulate soil-moisture measurements using a potentiometer in Wokwi.
3. Store sensor readings in a structured dataset.
4. Process environmental readings using Python.
5. Generate plant-specific recommendations.
6. Explore how the collected data could eventually support
   statistical analysis and machine-learning approaches.

---

## 🧠 Current System

```text
Environmental conditions
        ↓
     Sensors
        ↓
 Arduino / Wokwi
        ↓
 Temperature / Humidity / Soil Moisture
        ↓
     CSV Dataset
        ↓
       Python
        ↓
Data processing + rule-based interpretation
        ↓
Plant-specific recommendations
