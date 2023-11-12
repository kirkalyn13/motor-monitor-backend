from cursor import query

insert_query = """
INSERT INTO metrics (
    motor_id,
    line1_voltage,
    line2_voltage,
    line3_voltage,
    line1_current,
    line2_current,
    line3_current,
    temperature
) VALUES (
    1137, 220, 225, 215, 10, 15, 20, 75
);
"""
query(insert_query)

print("Test data added successfully.")
