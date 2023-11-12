from cursor import query

# Execute a simple SQL query
# Define the SQL query to create the 'metrics' table
create_table_query = """
CREATE TABLE metrics (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    motor_id TEXT,
    line1_voltage DOUBLE PRECISION,
    line2_voltage DOUBLE PRECISION,
    line3_voltage DOUBLE PRECISION,
    line1_current DOUBLE PRECISION,
    line2_current DOUBLE PRECISION,
    line3_current DOUBLE PRECISION,
    temperature DOUBLE PRECISION
);
"""

query("DROP TABLE IF EXISTS metrics;")
query(create_table_query)

print("Table 'metrics' created successfully.")
