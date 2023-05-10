from flask import (
    Blueprint, render_template, request, make_response
)

bp = Blueprint('some_operation', __name__, url_prefix='/op')

@bp.route('/', methods=['GET'])
def description():
    return render_template('some-operation.html')

@bp.route('/some-operation', methods=('GET', 'POST'))
def operation():
    if request.method == 'GET':
        response = make_response({
            "message": "Send data to this endpoint with an HTTP POST request to activate an operation on the data.",
            "accepts": "application/json",
            "returns": "application/json",
        })
        response.headers['Content-Type'] = 'application/json'
        response.headers['Content-Length'] = 176

        return response

    elif request.method == 'POST':
        data = request.get_json()

        # Here some operation happens on the data, then a response is sent.
        # In this template we just return a confirmation that the data is successfully received.

        print(data)

        response = make_response({ "message": "Data received successfully" })
        response.headers['Content-Type'] = 'application/json'
        response.headers['Content-Length'] = 46

        return response
    
    


