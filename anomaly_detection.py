def detect_anomaly(data):
    anomalies = {}
    if data['temperature'] > 80.0:
        anomalies['temperature'] = 'High'
    if data['cpu_usage'] > 90.0:
        anomalies['cpu_usage'] = 'High'
    if data['network_traffic'] > 900.0:
        anomalies['network_traffic'] = 'High'
    return anomalies