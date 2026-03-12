from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data['name']
    phone = data['phone']
    emergency = data['emergency']

    return jsonify({"message": "User saved successfully"})

if __name__ == '__main__':
    app.run(debug=True)