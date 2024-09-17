from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/service_a', methods=['GET'])
def service_a():
    response = requests.get(
        'http://service-b:5001/service_b')  # calling Service B
    return jsonify({
        'service': 'A',
        'response_from_b': response.json()
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
