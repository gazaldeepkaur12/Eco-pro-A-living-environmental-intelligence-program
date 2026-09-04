# Eco-pro 🌱
### A living environmental intelligence project

> A project that evolves with me.

Eco-pro started as a simple Python garden assistant and is growing into a small environmental monitoring system combining **Python, Arduino, sensors and environmental data**.

The idea is simple: collect environmental data, understand what it means for different plants, and turn it into useful recommendations.

---

## 🌱 What it does

Eco-pro currently:

- Reads temperature, humidity and soil moisture
- Uses Arduino/Wokwi for sensor simulation
- Stores readings in CSV format
- Uses Python to process the data
- Compares conditions with plant-specific ranges
- Gives simple recommendations based on the readings
- Keeps a history of environmental measurements

Currently supported plant profiles:

**🍅 Tomato · 🌿 Basil · 🌵 Cactus · 🌱 Fern**

---

## ⚙️ How it works

```text
Arduino / Wokwi
      ↓
Temperature + Humidity + Soil Moisture
      ↓
      CSV
      ↓
   Python
      ↓
Plant profile + environmental conditions
      ↓
Recommendation
```

---

## 🛠️ Tech

- Python
- Arduino / C++
- Wokwi
- CSV
- Git & GitHub

---

## 📁 Repository

```text
arduino/       Arduino sensor code + documentation
data/          Sensor data + data dictionary
python/        Python garden assistant
simulation/    Wokwi simulation files
analysis/      Graphs from the simulated dataset
README.md      Project overview
```

---

## 📊 Data and analysis

The current dataset contains **simulated observations** from the Wokwi-based project. The graphs in `analysis/` show how temperature, humidity and soil-moisture values vary across the four plant profiles.

These values are useful for demonstrating the data-processing workflow, but they should not be treated as real-world calibrated environmental measurements.

---

## 🚧 What's next

- Collect real sensor data
- Add environmental trend analysis
- Visualize changes over time
- Test the system with physical hardware
- Connect the Arduino and Python systems

---

## 💡 Why I'm building it

I'm interested in what happens when **biology, environmental science and technology overlap**.

Eco-pro is my way of learning that intersection by building things and improving them as I learn.

---

**Built and documented by Gazaldeep Kaur**

*This project is a work in progress.*
