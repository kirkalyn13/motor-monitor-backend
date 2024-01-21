from datetime import datetime, timedelta
import pytz

TIMEZONE = 'Asia/Manila'

timestamp_format = f"""
    timestamp
    AT TIME ZONE 'UTC'
    AT TIME ZONE
    '{TIMEZONE}' 
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

def generate_timestamps(period):
    tz_mnl = pytz.timezone(TIMEZONE)
    current_time = datetime.now(tz_mnl) - timedelta(minutes = 1)
    start_time = current_time - timedelta(minutes = period)
    timestamps = [(start_time + timedelta(minutes = i)).strftime("%m/%d - %H:%M") for i in range(period + 1)]

    return timestamps

def revert_timestamp(input_timestamp):
    parsed_timestamp = datetime.strptime(input_timestamp, "%m/%d - %H:%M")
    current_year = datetime.now().year
    parsed_timestamp = parsed_timestamp.replace(year=current_year)
    gmt_timezone = pytz.timezone('GMT')
    parsed_timestamp = gmt_timezone.localize(parsed_timestamp)
    reverted_timestamp = parsed_timestamp.strftime('%a, %d %b %Y %H:%M:%S GMT')
    
    return reverted_timestamp