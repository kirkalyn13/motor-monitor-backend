from datetime import datetime, timedelta

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

def get_timestamp_range(period = 15):
    current_time = datetime.utcnow()
    start_time = current_time - timedelta(minutes = period)

    start_timestamp_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
    end_timestamp_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

    return "'" + start_timestamp_str + "' AND '" + end_timestamp_str + "'"