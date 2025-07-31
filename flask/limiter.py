from flask import Flask, request, jsonify
from functools import wraps
import time

app = Flask(__name__)
visitors = {}

def rate_limit(max_requests, window_seconds):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            ip = request.remote_addr
            now = time.time()
            if ip not in visitors:
                visitors[ip] = []
            visitors[ip] = [t for t in visitors[ip] if now - t < window_seconds]

            if len(visitors[ip]) >= max_requests:
                return jsonify({"error": "Too many requests"}), 429

            visitors[ip].append(now)
            return f(*args, **kwargs)
        return wrapped
    return decorator

@app.route('/limited')
@rate_limit(5, 60)  
def limited_route():
    return "This route is rate-limited."

if __name__ == '__main__':
    app.run()