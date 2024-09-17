import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/service_a', methods=['GET'])
def service_a():
    response_b = requests.get('http://service-b:5001/service_b').json()
    response_c = requests.get('http://service-c:5002/service_c').json()
    response_d = requests.get('http://service-d:5003/service_d').json()
    response_e = requests.get('http://service-e:5004/service_e').json()

    return jsonify({
        "service": "A",
        "response_from_b": response_b,
        "response_from_c": response_c,
        "response_from_d": response_d,
        "response_from_e": response_e
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
