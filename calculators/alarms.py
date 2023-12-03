# Diagnostic computation; Identify possible motor problem from latest data
# Functions are divided per diagnosis/alarm
import utilities.severities as severity

def check_over_voltage(voltage, threshold):
    if voltage >= (1.15*threshold):
        return severity.CRITICAL
    elif voltage >= (1.1*threshold):
        return severity.WARNING
    else:
        return severity.NORMAL
    
def check_under_voltage(voltage, threshold):
    if voltage <= (0.85*threshold):
        return severity.CRITICAL
    elif voltage <= (0.9*threshold):
        return severity.WARNING
    else:
        return severity.NORMAL
    
def check_short_circuit(current, threshold):
    if current >= (threshold*4):
        return severity.CRITICAL
    else:
        return severity.NORMAL
    
def check_open_circuit(current):
    if current == 0:
        return severity.CRITICAL
    else:
        return severity.NORMAL
    
def check_temperature(temperature, threshold):
    if temperature >= threshold:
        return severity.CRITICAL
    elif temperature >= (0.9*threshold):
        return severity.WARNING
    else:
        return severity.NORMAL
    