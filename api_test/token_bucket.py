import time
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity          
        self.refill_rate = refill_rate   
        self.tokens = capacity          
        self.last_refill = time.time()

    def consume(self, tokens=1):
        now = time.time()
        elapsed = now - self.last_refill

        refill_amount = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + refill_amount)
        self.last_refill = now

        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

buckets = {}

CAPACITY = 5       
REFILL_RATE = 1    

def rate_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        client_ip = request.remote_addr
        if client_ip not in buckets:
            buckets[client_ip] = TokenBucket(CAPACITY, REFILL_RATE)

        bucket = buckets[client_ip]

        if not bucket.consume():
            return jsonify({"error": "Too many requests, slow down."}), 429

        return func(*args, **kwargs)
    return wrapper

@app.route('/api/data')
@rate_limit
def get_data():
    return jsonify({"data": "Here is your data"})

if __name__ == '__main__':
    app.run(debug=True, port=8000)