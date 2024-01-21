# Non-diagnostic computation; identify only status of latest data
# Functions are divided per motor parameter
import utilities.severities as severity

def get_voltage_status(value, threshold):
    if value >= (1.15*threshold):
        return severity.CRITICAL
    elif value >= (1.1*threshold):
        return severity.WARNING
    elif value <= (0.85*threshold):
        return severity.CRITICAL
    elif value <= (0.9*threshold):
        return severity.WARNING
    elif value == 0:
        return severity.NULL
    else:
        return severity.NORMAL
    
def get_current_status(value, threshold):
    if value >= (1.25*threshold):
        return severity.CRITICAL
    elif value == 0:
        return severity.NULL
    else:
        return severity.NORMAL
    
def get_temperature_status(value, threshold):
    if value >= threshold:
        return severity.CRITICAL
    elif value == 0:
        return severity.NULL
    elif value >= (0.9*threshold):
        return severity.WARNING
    else:
        return severity.NORMAL