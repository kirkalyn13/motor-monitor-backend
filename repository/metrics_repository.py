from db.cursor import query

def get_latest_metrics(id):
    query_string = f"""
        SELECT * FROM metrics
        WHERE motor_id = '{id}'
        ORDER BY timestamp DESC
        LIMIT 1;
        """
    print(query(query_string))
    return query(query_string)
