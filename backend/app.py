from flask import Flask, request, jsonify

app = Flask(__name__)

# List untuk menyimpan riwayat log data (penyimpanan sementara untuk MVP)
sensor_logs = []

@app.route('/api/telemetry', methods=['POST'])
def receive_telemetry():
    data = request.json
    if not data or 'water state' not in data:
        return jsonify({"error": "Invalid data format"}), 400
    
    # Menambahkan data ke dalam riwayat log
    sensor_logs.append(data)
    
    return jsonify({"status": "success", "message": "Data telemetry saved successfully"}), 200

@app.route('/api/telemetry/latest', methods=['GET'])
def get_latest_telemetry():
    if not sensor_logs:
        return jsonify({"error": "No data available"}), 404
    # Mengembalikan data telemetri terbaru
    return jsonify(sensor_logs[-1]), 200

@app.route('/api/telemetry/history', methods=['GET'])
def get_telemetry_history():
    # Mengembalikan seluruh riwayat data yang tersimpan
    return jsonify(sensor_logs), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
