from flask import Flask, request
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(
    filename='connections_log',  
    level=logging.INFO,  
    format='%(asctime)s - %(message)s',  
)

@app.route('/')
def home():
    log_request() 
    return "Welcome to the Server!"

@app.route('/register')
def register():
    log_request()  
    return "Registration Page"

@app.route('/login')
def login():
    log_request() 
    return "Login Page"

def log_request():
    ip = request.remote_addr  
    user_agent = request.user_agent.string  
    method = request.method  
    path = request.path 

    log_message = f"IP: {ip} | Method: {method} | Path: {path} | User-Agent: {user_agent}"
    logging.info(log_message)  

    print(log_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
