import random

def get_sensor_data():
    return {
        'temperature': round(random.uniform(20.0, 100.0), 2),
        'cpu_usage': round(random.uniform(0.0, 100.0), 2),
        'network_traffic': round(random.uniform(10.0, 1000.0), 2)
    }