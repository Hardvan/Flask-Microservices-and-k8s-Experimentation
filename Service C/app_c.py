from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/service_c', methods=['GET'])
def service_c():
    return jsonify({
        "service": "C",
        "message": "Hello from Service C"
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
