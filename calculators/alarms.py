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
    
def check_null_readings(timestamp, voltages, currents, temperature):
    null_alarms = []
    if voltages[0] == 0:
        null_alarms.append({
            "timestamp": timestamp,
            "alarm": "No Data for Phase 1 Voltage",
            "status": severity.NULL
        })
    if voltages[1] == 0:
        null_alarms.append({
            "timestamp": timestamp,
            "alarm": "No Data for Phase 2 Voltage",
            "status": severity.NULL
        })
    if voltages[2] == 0:
        null_alarms.append({
            "timestamp": timestamp,
            "alarm": "No Data for Phase 3 Voltage",
            "status": severity.NULL
        })
    if currents[0] == 0:
        null_alarms.append({
            "timestamp": timestamp,
            "alarm": "No Data for Line 1 Current",
            "status": severity.NULL
        })
    if currents[1] == 0:
        null_alarms.append({
            "timestamp": timestamp,
            "alarm": "No Data for Line 2 Current",
            "status": severity.NULL
        })
    if currents[2] == 0:
        null_alarms.append({
            "timestamp": timestamp,
            "alarm": "No Data for Line 3 Current",
            "status": severity.NULL
        })
    if temperature == 0:
        null_alarms.append({
            "timestamp": timestamp,
            "alarm": "No Data for Temperature",
            "status": severity.NULL
        })

    return null_alarms