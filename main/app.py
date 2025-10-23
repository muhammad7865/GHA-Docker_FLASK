
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Health check route
@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200

# POST route for data
@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    return jsonify({
        "message": "Data received successfully!",
        "data": data
    }), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)