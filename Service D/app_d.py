from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/service_d', methods=['GET'])
def service_d():
    return jsonify({
        "service": "D",
        "status": "Service D is healthy"
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
