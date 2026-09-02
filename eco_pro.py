"""
Garden Assistant

Reads plant sensor data, timestamps readings, stores them in
garden_log.csv, and gives plant-specific advice.
"""

import csv
import os
from datetime import datetime


LOG_FILE = "garden_log.csv"

PLANTS = {
    "TOMATO_01": {
        "name": "tomato",
        "temp": (18, 27),
        "humidity": (50, 70),
        "soil": (40, 70),
    },
    "BASIL_01": {
        "name": "basil",
        "temp": (18, 30),
        "humidity": (40, 60),
        "soil": (40, 60),
    },
    "CACTUS_01": {
        "name": "cactus",
        "temp": (15, 35),
        "humidity": (10, 30),
        "soil": (10, 30),
    },
    "FERN_01": {
        "name": "fern",
        "temp": (16, 24),
        "humidity": (60, 90),
        "soil": (50, 80),
    },
}


def classify(value, low, high):
    span = high - low
    if value < low - span:
        return "CRITICAL LOW"
    if value < low:
        return "LOW"
    if value > high + span:
        return "CRITICAL HIGH"
    if value > high:
        return "HIGH"
    return "OPTIMAL"


def ensure_log_header():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as file:
            csv.writer(file).writerow(
                ["date", "time", "plant_id", "temp", "humidity", "soil"]
            )


def log_reading(plant_id, temp, humidity, soil):
    now = datetime.now()
    with open(LOG_FILE, "a", newline="") as file:
        csv.writer(file).writerow(
            [
                now.strftime("%Y-%m-%d"),
                now.strftime("%H:%M:%S"),
                plant_id,
                temp,
                humidity,
                soil,
            ]
        )


def give_advice(temp, humidity, soil, plant):
    if soil < plant["soil"][0]:
        return "Advice: soil is dry - time to water."
    if soil > plant["soil"][1]:
        return "Advice: soil is very wet - avoid watering."
    if temp > plant["temp"][1]:
        return "Advice: it is hot - some shade would help."
    if temp < plant["temp"][0]:
        return "Advice: temperature is low for this plant."
    if humidity < plant["humidity"][0]:
        return "Advice: air is dry - try misting the leaves."
    if humidity > plant["humidity"][1]:
        return "Advice: humidity is high - improve airflow."
    return "Advice: conditions look good."


def show_status(plant_id, temp, humidity, soil):
    if plant_id not in PLANTS:
        print("Unknown plant ID:", plant_id)
        return

    plant = PLANTS[plant_id]
    print("\n" + "=" * 45)
    print("Plant:", plant["name"])
    print("Plant ID:", plant_id)
    print(
        f"Temperature:   {temp} C -> "
        f"{classify(temp, *plant['temp'])}"
    )
    print(
        f"Humidity:      {humidity} % -> "
        f"{classify(humidity, *plant['humidity'])}"
    )
    print(
        f"Soil moisture: {soil} % -> "
        f"{classify(soil, *plant['soil'])}"
    )
    print(give_advice(temp, humidity, soil, plant))
    print("=" * 45)


def process_reading(data):
    data = data.strip()
    if not data or data == "plant_id,temp,humidity,soil":
        return

    parts = data.split(",")
    if len(parts) != 4:
        print("Invalid reading:", data)
        return

    plant_id = parts[0].strip()
    if plant_id not in PLANTS:
        print("Unknown plant ID:", plant_id)
        return

    try:
        temp = float(parts[1])
        humidity = float(parts[2])
        soil = float(parts[3])
    except ValueError:
        print("Invalid sensor values:", data)
        return

    log_reading(plant_id, temp, humidity, soil)
    show_status(plant_id, temp, humidity, soil)


def test_mode():
    test_readings = [
        "TOMATO_01,33.1,66.0,96",
        "TOMATO_01,44.8,75.0,70",
        "TOMATO_01,27.8,65.5,36",
        "TOMATO_01,32.0,79.5,62",
    ]

    print("\nRunning test data...")
    for reading in test_readings:
        process_reading(reading)


def show_csv():
    if not os.path.exists(LOG_FILE):
        print("No garden data found.")
        return

    print("\n=== Garden History ===")
    with open(LOG_FILE) as file:
        for row in csv.DictReader(file):
            print(
                row["date"],
                row["time"],
                "|",
                row["plant_id"],
                "|",
                row["temp"] + " C",
                "|",
                row["humidity"] + "%",
                "|",
                row["soil"] + "%",
            )


def live_mode():
    print("\nLive mode is not connected yet.")
    print("Wokwi/Arduino connection will be added here.")


def main():
    ensure_log_header()
    print("\n=== Garden Assistant ===")
    print("1) Run test sensor data")
    print("2) Show garden history")
    print("3) Live sensor mode")
    print("4) Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        test_mode()
    elif choice == "2":
        show_csv()
    elif choice == "3":
        live_mode()
    elif choice == "4":
        print("Goodbye.")
    else:
        print("Unknown option.")


if __name__ == "__main__":
    main()
