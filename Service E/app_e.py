from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/service_e', methods=['GET'])
def service_e():
    processed_data = "Data from Service E"
    return jsonify({
        "service": "E",
        "processed_data": processed_data
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
