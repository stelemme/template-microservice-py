from flask import (
    Blueprint, render_template, request, make_response
)
import datetime

# Initiating the blueprint and assigning to it the "/op/" URI
bp = Blueprint('some_operation', __name__, url_prefix='/op')

# Adding a function to the "/op/" URI
@bp.route('/', methods=['GET'])
def description():
    return render_template('some-operation.html')

# Adding a function to the "/op/some-operation" URI
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
        # The data is retrieved out of the incoming HTTP POST request.
        data = request.get_json()

        # Here some operation happens on the data.

        # The response data is added to the response
        response = make_response({ "message": "Data received successfully" })

        # The headers are defined properly. 
        response.headers['Date'] = datetime.datetime.now()
        response.headers['Server'] = 'My Werkzeug Server'
        response.headers['Content-Type'] = 'application/json'
        response.headers['Content-Length'] = 46

        # The response code is set, and the response is sent back to the requesting party.
        response.status_code = 200
        return response
    
    


