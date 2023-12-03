from datetime import datetime

timestamp_format = """
    timestamp
    AT TIME ZONE 'UTC'
    AT TIME ZONE
    'Asia/Manila' 
    AS ph_timestamp
    """

def convert_timestamp(timestamp):
    datetime_object = datetime.strptime(str(timestamp), "%Y-%m-%d %H:%M:%S.%f")
    return datetime_object.strftime("%m/%d - %H:%M")