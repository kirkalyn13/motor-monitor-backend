# Diagnostic computation; Identify possible motor problem from latest data
# Functions are divided per diagnosis/alarm
import utilities.severities as severity

PHASE_LOSS_TOLERANCE = 0.2

def check_over_voltage(voltage, threshold):
    if voltage >= (1.15*threshold):
        return severity.CRITICAL
    elif voltage >= (1.1*threshold):
        return severity.WARNING
    else:
        return severity.NORMAL
    
def check_under_voltage(voltage, threshold):
    if voltage <= (0.85*threshold) and voltage > (0.1*threshold):
        return severity.CRITICAL
    elif voltage <= (0.9*threshold) and voltage > (0.1*threshold):
        return severity.WARNING
    else:
        return severity.NORMAL
    
def check_no_power(voltage, threshold):
    if voltage <= (0.1*threshold):
        return severity.CRITICAL
    else:
        return severity.NORMAL
    
def check_short_circuit(current, threshold):
    if current >= (threshold*4):
        return severity.CRITICAL
    else:
        return severity.NORMAL
    
def check_phase_loss(current, threshold):
    if current >= (1.25*threshold):
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
    