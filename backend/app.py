from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary storage untuk MVP
latest_data = {}

@app.route('/api/telemetry', methods=['POST'])
def receive_telemetry():
    data = request.json
    # Validasi sederhana format data
    if not data or 'water state' not in data:
        return jsonify({"error": "Invalid data format"}), 400

    global latest_data
    latest_data = data
    return jsonify({"status": "success", "message": "Data saved"}), 200

@app.route('/api/telemetry/latest', methods=['GET'])
def get_latest_telemetry():
    if not latest_data:
        return jsonify({"error": "No data available"}), 404
    return jsonify(latest_data), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
