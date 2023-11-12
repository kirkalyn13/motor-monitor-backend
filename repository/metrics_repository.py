from db.cursor import query

def get_latest_metrics():
    query_string = """
        SELECT * FROM metrics
        ORDER BY timestamp DESC
        LIMIT 1;
        """
    print(query(query_string))
    return query(query_string)
