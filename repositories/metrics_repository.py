from db.cursor import query
from utilities.time import timestamp_format

def get_latest_metrics(id):
    query_string = f"""
        SELECT 
        {timestamp_format}, 
        motor_id,
        line1_voltage,
        line2_voltage,
        line3_voltage,
        line1_current,
        line2_current,
        line3_current,
        temperature 
        FROM metrics
        WHERE motor_id = '{id}'
        ORDER BY timestamp DESC
        LIMIT 1;
        """
    return query(query_string)

def get_voltage_trend(id, limit):
    query_string = f"""
        SELECT {timestamp_format}, line1_voltage, line2_voltage, line3_voltage 
        FROM metrics
        WHERE motor_id = '{id}'
        ORDER BY timestamp DESC
        LIMIT {limit};
        """
    return query(query_string)

def get_current_trend(id, limit):
    query_string = f"""
        SELECT {timestamp_format}, line1_current, line2_current, line3_current 
        FROM metrics
        WHERE motor_id = '{id}'
        ORDER BY timestamp DESC
        LIMIT {limit};
        """
    return query(query_string)

def get_temperature_trend(id, limit):
    query_string = f"""
        SELECT {timestamp_format}, temperature 
        FROM metrics
        WHERE motor_id = '{id}'
        ORDER BY timestamp DESC
        LIMIT {limit};
        """
    return query(query_string)

def add_metrics(id, line1_voltage, line2_voltage, line3_voltage, line1_current, line2_current, line3_current, temperature):
    query_string = f"""
        INSERT INTO metrics 
        (
        motor_id,
        line1_voltage,
        line2_voltage,
        line3_voltage,
        line1_current,
        line2_current,
        line3_current,
        temperature
        ) 
        VALUES 
        (
        '{id}',
        {line1_voltage},
        {line2_voltage},
        {line3_voltage},
        {line1_current},
        {line2_current},
        {line3_current},
        {temperature}
        );
        """
    return query(query_string, False)
