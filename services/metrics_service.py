import repositories.metrics_repository as metrics_repository
import utilities.severities as severity
import calculators.alarms as alarms
import calculators.status as status
from utilities.time import convert_timestamp

def get_latest_metrics(id, rated_voltage, rated_current, max_temperature):
    result = metrics_repository.get_latest_metrics(id)[0]
    latest_metrics = {
        "timestamp": result[0],
        "unitID": result[1],
        "line1Voltage": {
            "value": result[2],
            "status": status.get_voltage_status(result[2], rated_voltage)
        },
        "line2Voltage": {
            "value": result[3],
            "status": status.get_voltage_status(result[3], rated_voltage)
        },
        "line3Voltage": {
            "value": result[4],
            "status": status.get_voltage_status(result[4], rated_voltage)
        },
        "line1Current": {
            "value": result[5],
            "status": status.get_current_status(result[5], rated_current)
        },
        "line2Current": {
            "value": result[6],
            "status": status.get_current_status(result[6], rated_current)
        },
        "line3Current": {
            "value": result[7],
            "status": status.get_current_status(result[7], rated_current)
        },
        "temperature": {
            "value": result[8],
            "status": status.get_temperature_status(result[8], max_temperature)
        }
    }
    return latest_metrics

def get_voltage_trend(id):
    voltage_trend = [{
        "name": "Line 1 Voltage",
        "data": []
    },
    {
        "name": 'Line 2 Voltage',
        "data": []
    },
    {
        "name": "Line 3 Voltage",
        "data": []
    }]
    timestamps = []

    result = metrics_repository.get_voltage_trend(id)
    for data in result:
        timestamps.insert(0, convert_timestamp(data[0]))
        voltage_trend[0]["data"].insert(0, data[1])
        voltage_trend[1]["data"].insert(0, data[2])
        voltage_trend[2]["data"].insert(0, data[3])

    return {
        "trend": voltage_trend,
        "timestamps": timestamps
    }

def get_current_trend(id):
    current_trend = [{
        "name": "Line 1 Current",
        "data": []
    },
    {
        "name": 'Line 2 Current',
        "data": []
    },
    {
        "name": "Line 3 Current",
        "data": []
    }]
    timestamps = []

    result = metrics_repository.get_current_trend(id)
    for data in result:
        timestamps.insert(0, convert_timestamp(data[0]))
        current_trend[0]["data"].insert(0, data[1])
        current_trend[1]["data"].insert(0, data[2])
        current_trend[2]["data"].insert(0, data[3])

    return {
        "trend": current_trend,
        "timestamps": timestamps
    }

def get_temperature_trend(id):
    temperature_trend = [{
        "name": "Temperature",
        "data": []
    }]
    timestamps = []

    result = metrics_repository.get_temperature_trend(id)
    for data in result:
        timestamps.insert(0, convert_timestamp(data[0]))
        temperature_trend[0]["data"].insert(0, data[1])

    return {
        "trend": temperature_trend,
        "timestamps": timestamps
    }

def get_metrics_summary(id, rated_voltage, rated_current, max_temperature):
    result = metrics_repository.get_latest_metrics(id)[0]
    metrics_status = [
            status.get_voltage_status(result[2], rated_voltage),
            status.get_voltage_status(result[3], rated_voltage),
            status.get_voltage_status(result[4], rated_voltage),
            status.get_current_status(result[5], rated_current),
            status.get_current_status(result[6], rated_current),
            status.get_current_status(result[7], rated_current),
            status.get_temperature_status(result[8], max_temperature)
    ]

    normal_count = 0
    warning_count = 0
    critical_count = 0
    
    for alarm_status in metrics_status:
        if alarm_status == severity.NORMAL:
            normal_count += 1
        elif alarm_status == severity.WARNING:
            warning_count += 1
        elif alarm_status == severity.CRITICAL:
            critical_count += 1

    return {
        "summary": [ normal_count, warning_count, critical_count ]
    }

def get_alarms(id, rated_voltage, rated_current, max_temperature):
    result = metrics_repository.get_latest_metrics(id)[0]
    alarms_list = []

    # Over Voltage
    if alarms.check_over_voltage(result[2], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 1 Over Voltage",
            "status": alarms.check_over_voltage(result[2], rated_voltage)
        })
    if alarms.check_over_voltage(result[3], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 2 Over Voltage",
            "status": alarms.check_over_voltage(result[3], rated_voltage)
        })
    if alarms.check_over_voltage(result[4], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 3 Over Voltage",
            "status": alarms.check_over_voltage(result[4], rated_voltage)
        })

    # Under Voltage
    if alarms.check_under_voltage(result[2], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 1 Under Voltage",
            "status": alarms.check_under_voltage(result[2], rated_voltage)
        })
    if alarms.check_under_voltage(result[3], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 2 Under Voltage",
            "status": alarms.check_under_voltage(result[3], rated_voltage)
        })
    if alarms.check_under_voltage(result[4], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 3 Under Voltage",
            "status": alarms.check_under_voltage(result[4], rated_voltage)
        })

    # Short Circuit
    if alarms.check_short_circuit(result[5], rated_current) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 1 Short Circuit",
            "status": alarms.check_short_circuit(result[5], rated_current)
        })
    if alarms.check_short_circuit(result[6], rated_current) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 2 Short Circuit",
            "status": alarms.check_short_circuit(result[6], rated_current)
        })
    if alarms.check_short_circuit(result[7], rated_current) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 3 Short Circuit",
            "status": alarms.check_short_circuit(result[7], rated_current)
        })
    
    # No Output
    if alarms.check_no_output(result[2]) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 1 No Output",
            "status": alarms.check_no_output(result[2])
        })
    if alarms.check_no_output(result[3]) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 2 No Output",
            "status": alarms.check_no_output(result[3])
        })
    if alarms.check_no_output(result[4]) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 3 No Output",
            "status": alarms.check_no_output(result[4])
        })

    # Open Circuit
    if alarms.check_open_circuit(result[5]) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 1 Open Circuit",
            "status": alarms.check_open_circuit(result[5])
        })
    if alarms.check_open_circuit(result[6]) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 2 Open Circuit",
            "status": alarms.check_open_circuit(result[6])
        })
    if alarms.check_open_circuit(result[7]) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Line 3 Open Circuit",
            "status": alarms.check_open_circuit(result[7])
        })

    # Temperature
    if alarms.check_temperature(result[8], max_temperature) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Overheating",
            "status": alarms.check_temperature(result[8], max_temperature)
        })

    # Phase Loss
    if alarms.check_phase_loss(result[5]) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Phase Loss",
            "status": alarms.check_phase_loss(result[5])
        })
    elif alarms.check_phase_loss(result[6]) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Phase Loss",
            "status": alarms.check_phase_loss(result[6])
        })
    elif alarms.check_phase_loss(result[7]) != severity.NORMAL:
        alarms_list.append({
            "alarm": "Phase Loss",
            "status": alarms.check_phase_loss(result[7])
        })

    return alarms_list

def add_metrics(id, line1_voltage, line2_voltage, line3_voltage, line1_current, line2_current, line3_current, temperature):
    metrics_repository.add_metrics(id, line1_voltage, line2_voltage, line3_voltage, line1_current, line2_current, line3_current, temperature)
    return { "metrics": [ id, line1_voltage, line2_voltage, line3_voltage, line1_current, line2_current, line3_current, temperature ] }
        
