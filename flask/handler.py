from flask import Flask, jsonify

app = Flask(__name__)

class CustomError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

@app.errorhandler(CustomError)
def handle_custom_error(error):
    response = {
        "error": error.message
    }
    return jsonify(response), error.status_code

@app.route('/raise-error')
def raise_error():
    raise CustomError("This is a custom error message", 422)

if __name__ == "__main__":
    app.run(debug=True)