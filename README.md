# Eco-pro 🌱

### A low-cost environmental sensing and computational decision-support experiment

Eco-pro is an evolving environmental sensing project exploring how
low-cost sensors, embedded systems, and computational methods can be
used to monitor and interpret changing environmental conditions.

The project currently uses an Arduino-based sensing system, simulated
in Wokwi, to collect temperature, relative humidity, and soil-moisture
measurements. These observations are processed using Python and
translated into simple plant-specific recommendations.

Rather than beginning with machine learning, Eco-pro starts with a
transparent rule-based baseline. This creates a simple system whose
assumptions can be examined before introducing more complex
data-driven methods.

---

## 🔬 Research Question

**How can low-cost environmental sensing and computational methods
be used to monitor changing micro-environmental conditions and
translate measurements into useful environmental decisions?**

---

## 🎯 Objectives

- Design a low-cost environmental sensing system.
- Simulate sensor acquisition using Arduino and Wokwi.
- Collect structured environmental observations.
- Process environmental data using Python.
- Develop transparent rule-based decision logic.
- Examine the limitations of simulated environmental data.
- Establish a baseline for future statistical and machine-learning
  approaches.

---

## 🧠 Why Eco-pro?

Environmental systems are dynamic and difficult to represent using
single measurements or fixed assumptions.

Eco-pro began as a small Python garden assistant and has developed
into an experiment in connecting:

**sensing → data → computation → decision-making**

The current system is deliberately simple. Its purpose is to provide
a transparent baseline that can later be tested against more
data-driven approaches.

---

## ⚙️ System Overview

```text
        Environmental conditions
                  ↓
             DHT22 sensor
                  +
        Soil-moisture simulation
                  ↓
             Arduino Nano
                  ↓
          Sensor observations
                  ↓
             CSV dataset
                  ↓
               Python
                  ↓
        Rule-based interpretation
                  ↓
       Plant-specific recommendation
