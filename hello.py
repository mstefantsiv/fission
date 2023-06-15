from flask import request, jsonify


def main():
    params = request.get_json()
    return jsonify(params)
