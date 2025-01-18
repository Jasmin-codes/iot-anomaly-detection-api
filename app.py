from flask import Flask, jsonify
from sensor_simulator import get_sensor_data
from anomaly_detection import detect_anomaly

app = Flask(__name__)

@app.route('/sensor-data', methods=['GET'])
def sensor_data():
    data = get_sensor_data()
    anomalies = detect_anomaly(data)
    return jsonify({'data': data, 'anomalies': anomalies})

if __name__ == '__main__':
    app.run(debug=True)