"""
Test script for Smart Sensor Monitoring System

This script simulates the sensor data generation and threshold checking
that happens in the n8n workflow. Useful for testing without n8n.
"""
import random
from datetime import datetime

def generate_sensor_data():
    """Generate simulated sensor data."""
    return {
        "temperature": random.randint(0, 100),  # 0 to 99°C
        "humidity": random.randint(0, 100),     # 0 to 99%
        "gasLevel": round(random.uniform(0, 1.2), 2),  # 0.00 to ~1.2
        "timestamp": datetime.now().isoformat()
    }

def check_thresholds(data):
    """Check if any thresholds are exceeded."""
    temp_high = data["temperature"] > 50
    gas_high = data["gasLevel"] > 0.5
    
    if temp_high or gas_high:
        status = "ALERT"
        message = """🚨 Sensor Alert!
🌡️ Temperature: {temperature}°C
🧪 Gas Level: {gasLevel}
⏱️ Time: {timestamp}""".format(**data)
    else:
        status = "NORMAL"
        message = "✅ All parameters normal"
    
    return status, message

def main():
    """Run a test simulation."""
    print("=== Smart Sensor Test ===\n")
    
    # Generate test data
    data = generate_sensor_data()
    print("Generated Sensor Data:")
    for key, value in data.items():
        print(f"- {key}: {value}")
    
    # Check thresholds
    status, message = check_thresholds(data)
    print(f"\nStatus: {status}")
    print(message)

if __name__ == "__main__":
    main()
