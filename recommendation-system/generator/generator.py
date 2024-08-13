from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    model_name = data.get('model_name')
    viewerid = data.get('viewerid')
    
    random_number = random.randint(1, 100)
    
    response = {
        "reason": model_name,
        "result": random_number
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
