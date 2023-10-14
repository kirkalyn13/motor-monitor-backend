from datetime import datetime

def error(message):
    current_timestamp = datetime.now()
    error = {
        "statusCode": 500,
        "message": message,
        "timestamp": current_timestamp
    }
    return error