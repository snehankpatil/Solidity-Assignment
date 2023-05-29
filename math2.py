from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify(error='Invalid payload'), 400
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 + num2
        return jsonify(result=result), 200
    except ValueError:
        return jsonify(error='Invalid numbers'), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
