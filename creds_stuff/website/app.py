from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key' 

users = {
    'admin': 'admin',  
    'user': 'user',
    'service': 'service',
    'support': 'support'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))  
    else:
        flash('Invalid username or password. Please try again.', 'error')
        return redirect(url_for('home')) 

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
