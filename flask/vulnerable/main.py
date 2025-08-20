from flask import Flask, request, jsonify
import traceback

app = Flask(__name__)

FAKE_DATABASE = {
    "users": [
        {"id": 1, "email": "admin@example.com"},
        {"id": 2, "email": "user@example.com"}
    ]
}

@app.route('/api/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test_endpoint():
    try:
        response_data = {"message": "Welcome to the test API!"}

        response_data["database_info"] = FAKE_DATABASE["users"]

        if request.args.get('id'):
            id_param = request.args.get('id')
            if "'" in id_param:
                response_data["error"] = f"SQL Syntax Error: Invalid query near '{id_param}'"
            else:
                response_data["id_query"] = f"Queried ID: {id_param}"

        if request.args.get('q'):
            query = request.args.get('q')
            response_data["search_result"] = f"Search: {query}"

        response_data["method"] = f"Received {request.method} request"

        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS"
        }

        if request.args.get('invalid_param'):
            raise Exception("Invalid parameter provided")

        return jsonify(response_data), 200, headers

    except Exception as e:
        error_response = {
            "error": "Internal Server Error",
            "details": str(e),
            "stack_trace": traceback.format_exc()
        }
        return jsonify(error_response), 500, {"Access-Control-Allow-Origin": "*"}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)