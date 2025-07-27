import time
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

request_times = {}

MAX_REQUESTS = 5
TIME_WINDOW = 60  

def rate_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        client_ip = request.remote_addr
        now = time.time()

        if client_ip not in request_times:
            request_times[client_ip] = []

        request_times[client_ip] = [t for t in request_times[client_ip] if now - t < TIME_WINDOW]

        if len(request_times[client_ip]) >= MAX_REQUESTS:
            return jsonify({"error": "Too many requests, slow down."}), 429

        request_times[client_ip].append(now)

        return func(*args, **kwargs)
    return wrapper

@app.route('/api/data')
@rate_limit
def get_data():
    return jsonify({"data": "Here is your data"})

if __name__ == '__main__':
    app.run(debug=True)