from os import getenv
from dotenv import load_dotenv

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import WebApplicationClient
from flask import Flask, request, redirect

load_dotenv()

CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')
AUTHORIZATION_BASE_URL = 'https://provider.com/oauth/authorize'
TOKEN_URL = 'https://provider.com/oauth/token'
REDIRECT_URI = 'http://localhost:5000/callback'

client = WebApplicationClient(CLIENT_ID)
oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)

app = Flask(__name__)

@app.route('/')
def login():
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    authorization_response = request.url
    
    oauth.fetch_token(TOKEN_URL, authorization_response=authorization_response, client_secret=CLIENT_SECRET)
    
    response = oauth.get('https://provider.com/api/user')
    return f'User info: {response.json()}'

if __name__ == '__main__':
    app.run(debug=True)