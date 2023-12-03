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
    if voltage <= (0.85*threshold):
        return severity.CRITICAL
    elif voltage <= (0.9*threshold):
        return severity.WARNING
    else:
        return severity.NORMAL
    
def check_no_output(voltage):
    if voltage == 0:
        return severity.CRITICAL
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
    
def check_phase_loss(current):
    if current >= (1.5*current):
        return severity.CRITICAL
    elif current >= (1.25*current):
        return severity.WARNING
    else:
        return severity.NORMAL
    
def check_temperature(temperature, threshold):
    if temperature >= threshold:
        return severity.CRITICAL
    elif temperature >= (0.9*threshold):
        return severity.WARNING
    else:
        return severity.NORMAL
    
def check_three_phase_loss(lines):
    if len(lines) != 3:
        raise ValueError("Expected a list with exactly three numbers.")

    lines.sort()
    tolerance = PHASE_LOSS_TOLERANCE * lines[1]

    diff_1_2 = abs(lines[1] - lines[0]) <= tolerance
    diff_2_3 = abs(lines[2] - lines[1]) <= tolerance

    return diff_1_2 and diff_2_3
    