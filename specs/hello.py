from flask import current_app

def main():
    current_app.logger.info("This is a log message")
    return "Hello, world"