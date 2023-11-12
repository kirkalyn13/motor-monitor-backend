from db.cursor import query

def get_latest_metrics(id):
    query_string = f"""
        SELECT * FROM metrics
        WHERE motor_id = '{id}'
        ORDER BY timestamp DESC
        LIMIT 1;
        """
    return query(query_string)

def get_voltage_trend(id):
    query_string = f"""
        SELECT line1_voltage, line2_voltage, line3_voltage 
        FROM metrics
        WHERE motor_id = '{id}'
        ORDER BY timestamp DESC
        LIMIT 12;
        """
    return query(query_string)
