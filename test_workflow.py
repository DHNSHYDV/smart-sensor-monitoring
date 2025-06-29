"""
Unit tests for the Smart Sensor Monitoring System
"""
import pytest
from test_sensor import generate_sensor_data, check_thresholds

def test_generate_sensor_data():
    """Test that sensor data is generated with expected keys and types."""
    data = generate_sensor_data()
    
    assert isinstance(data["temperature"], int)
    assert isinstance(data["humidity"], int)
    assert isinstance(data["gasLevel"], float)
    assert "timestamp" in data
    
    # Check value ranges
    assert 0 <= data["temperature"] <= 100
    assert 0 <= data["humidity"] <= 100
    assert 0 <= data["gasLevel"] <= 1.2

def test_check_thresholds_alert():
    """Test threshold checking with alert conditions."""
    # Test high temperature
    high_temp = {"temperature": 75, "gasLevel": 0.3, "timestamp": "2025-06-29T12:00:00"}
    status, _ = check_thresholds(high_temp)
    assert status == "ALERT"
    
    # Test high gas
    high_gas = {"temperature": 40, "gasLevel": 0.8, "timestamp": "2025-06-29T12:00:00"}
    status, _ = check_thresholds(high_gas)
    assert status == "ALERT"

def test_check_thresholds_normal():
    """Test threshold checking with normal conditions."""
    normal_data = {"temperature": 25, "gasLevel": 0.3, "timestamp": "2025-06-29T12:00:00"}
    status, _ = check_thresholds(normal_data)
    assert status == "NORMAL"
