# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request


def books_postHandler():

    inputs = request.get_json()

    return jsonify()
