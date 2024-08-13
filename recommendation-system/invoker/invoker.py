from flask import Flask, jsonify, request
import requests
import redis
import threading
from cachetools import TTLCache

app = Flask(__name__)

local_cache = TTLCache(maxsize=3, ttl=10)

redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    viewerid = data.get('viewerid')
    
    if viewerid in local_cache:
        return jsonify(local_cache[viewerid])
    
    cache_data = redis_client.get(viewerid)
    if cache_data:
        return jsonify(eval(cache_data))
    
    recommendations = runcascade(viewerid)
    
    local_cache[viewerid] = recommendations
    redis_client.set(viewerid, str(recommendations), ex=60) 
    
    return jsonify(recommendations)

def runcascade(viewerid):
    models = ['model1', 'model2', 'model3', 'model4', 'model5']
    threads = []
    results = []

    def fetch_model(model):
        response = requests.post('http://generator:5000/generate', json={'model_name': model, 'viewerid': viewerid})
        results.append(response.json())

    for model in models:
        thread = threading.Thread(target=fetch_model, args=(model,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return {'viewerid': viewerid, 'recommendations': results}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
