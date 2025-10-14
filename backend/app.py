from flask import Flask, jsonify, render_template, request
import json
from datetime import datetime

app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/process", methods=["POST"])
def process_text():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing text data"}), 400
    text = data.get("text", "")
    # Simulate NLP processing
    processed_text = f"Processed: {text.upper()}"
    return jsonify({"original_text": text, "processed_text": processed_text})

@app.route("/api/analytics")
def get_analytics():
    # Simulate fetching analytics results
    return jsonify({"analytics_data": "Some analytics data here"})

@app.route("/api/upload", methods=["POST"])
def upload_file():
    # Simulate file upload handling
    return jsonify({"message": "File uploaded successfully"})

@app.route("/api/status")
def status():
    return jsonify({"status": "running", "version": "1.0.0", "timestamp": datetime.now().isoformat()})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

