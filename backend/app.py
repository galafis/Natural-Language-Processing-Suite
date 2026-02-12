from flask import Flask, jsonify, render_template, request
from config import APP_CONFIG
from datetime import datetime

app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")

# Configure max content length
app.config['MAX_CONTENT_LENGTH'] = APP_CONFIG.get('max_content_length', 16 * 1024 * 1024)

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({"error": "File too large. Maximum size is 16MB."}), 413

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/process", methods=["POST"])
def process_text():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Invalid JSON data"}), 400
    
    if not data or "text" not in data:
        return jsonify({"error": "Missing text data"}), 400
    
    try:
        text = data.get("text", "")
        if not isinstance(text, str):
            return jsonify({"error": "Text must be a string"}), 400
        
        if len(text) > 10000:
            return jsonify({"error": "Text too long. Maximum 10,000 characters."}), 400
        
        # Simulate NLP processing
        processed_text = f"Processed: {text.upper()}"
        return jsonify({
            "original_text": text,
            "processed_text": processed_text,
            "length": len(text),
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({"error": f"Processing error: {str(e)}"}), 500

@app.route("/api/analytics")
def get_analytics():
    try:
        # Simulate fetching analytics results
        return jsonify({
            "analytics_data": "Some analytics data here",
            "records_processed": 1234,
            "last_updated": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({"error": f"Analytics error: {str(e)}"}), 500

@app.route("/api/upload", methods=["POST"])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"message": "No file provided, but endpoint is ready"}), 200
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        # Simulate file upload handling
        return jsonify({
            "message": "File uploaded successfully",
            "filename": file.filename,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({"error": f"Upload error: {str(e)}"}), 500

@app.route("/api/status")
def status():
    return jsonify({
        "status": "running",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "endpoints": ["/", "/api/process", "/api/analytics", "/api/upload", "/api/status"]
    })

if __name__ == "__main__":
    app.run(
        debug=APP_CONFIG.get('debug', True),
        host=APP_CONFIG.get('host', '0.0.0.0'),
        port=APP_CONFIG.get('port', 5000)
    )
