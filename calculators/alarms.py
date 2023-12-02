NORMAL = "normal"
WARNING = "warning"
CRITICAL = "critical"

def check_over_voltage(voltage, threshold):
    if voltage >= (1.1*threshold):
        return WARNING
    elif voltage >= (1.15*threshold):
        return CRITICAL
    else:
        return NORMAL
    
def check_under_voltage(voltage, threshold):
    if voltage <= (0.9*threshold):
        return WARNING
    elif voltage <= (0.85*threshold):
        return CRITICAL
    else:
        return NORMAL
    
def check_short_circuit(current, threshold):
    if current >= (threshold*4):
        return CRITICAL
    else:
        return NORMAL
    
def check_temperature(temperature, threshold):
    if temperature > (0.9*threshold):
        return WARNING
    elif temperature <= threshold:
        return CRITICAL
    else:
        return NORMAL
    