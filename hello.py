from flask import request
from flask import current_app

def main():
    current_app.logger.info(request.get_data())
    return "HI!"
