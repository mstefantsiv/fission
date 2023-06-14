from flask import requests

def main():
    current_app.logger.info("Received request")
    msg = "--BODY--\n%s\n-----\n" % (request.get_data())
    return msg
