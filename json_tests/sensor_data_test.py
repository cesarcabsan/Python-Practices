import json
from datetime import datetime

# Scenario: Logging Sensor Data into JSON
# Imagine you’re building a small data pipeline to collect environmental sensor readings (temperature, humidity, and air quality) from IoT devices. 
# You want to store these readings in a JSON file for later analysis

# Step 1: Simulated sensor readings
sensor_data = [
    {"sensor_id": "temp_01", "temperature": 22.5, "unit": "C"},
    {"sensor_id": "hum_02", "humidity": 45, "unit": "%"},
    {"sensor_id": "airq_03", "air_quality_index": 72, "unit": "AQI"}
]

# Step 2: Add metadata (timestamp + location)

data_package = {
    "timestamp": datetime.now().isoformat(),
    "location": "Monterrey, MX",
    "readings": sensor_data
}

# Step 3: Write to JSON file
with open("sensor_log.json", "w") as f:
    json.dump(data_package, f, indent=4)

print("Sensor data successfully written to sensor_log.json file")