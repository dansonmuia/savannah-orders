from flask import jsonify


def create_response(data, status_code):
    response = jsonify(data)
    response.status_code = status_code
    return response


def http_200(data):
    return create_response(data, 200)


def http_201(data):
    return create_response(data, 201)


def http_400(data):
    return create_response(data, 400)


def http_401(error='Unauthorised operation'):
    return create_response({'error': error}, 401)


def http_404(error='We cannot find a record matching your request'):
    return create_response({'error': error}, 404)


def http_405(error='Method not supported'):
    return create_response({'error': error}, 405)


def form_errors(form):
    return http_400({'errors': form.errors})


def field_errors(field, *errors):
    errors = {field: errors}
    return http_400({'errors': errors})
