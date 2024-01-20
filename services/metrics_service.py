import repositories.metrics_repository as metrics_repository
import utilities.severities as severity
import calculators.alarms as alarms
import calculators.status as status
from utilities.time import convert_timestamp, generate_timestamps

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

def get_voltage_trend(id, limit):
    voltage_trends = ["Phase 1 Voltage", "Phase 2 Voltage", "Phase 3 Voltage"]
    result = metrics_repository.get_voltage_trend(id, limit)
    return generate_trend(result, voltage_trends, limit)

def get_current_trend(id, limit):
    current_trends = ["Line 1 Current", "Line 2 Current", "Line 3 Current"]
    result = metrics_repository.get_current_trend(id, limit)
    return generate_trend(result, current_trends, limit)

def get_temperature_trend(id, limit):
    temperature_trends = ["Temperature"]
    result = metrics_repository.get_temperature_trend(id, limit)
    return generate_trend(result, temperature_trends, limit)

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
    alarms_list = analyze_metrics(result, rated_voltage, rated_current, max_temperature)
    return alarms_list

def add_metrics(id, line1_voltage, line2_voltage, line3_voltage, line1_current, line2_current, line3_current, temperature):
    metrics_repository.add_metrics(id, line1_voltage, line2_voltage, line3_voltage, line1_current, line2_current, line3_current, temperature)

    return { "metrics": [ id, line1_voltage, line2_voltage, line3_voltage, line1_current, line2_current, line3_current, temperature ] }

def get_metrics_logs(id, limit):
    logs = []

    result = metrics_repository.get_metrics_logs(id, limit)
    for data in result:
        logs.insert(0, {
            "timestamp": data[1],
            "id": data[2],
            "line1_voltage": data[3],
            "line2_voltage": data[4],
            "line3_voltage": data[5],
            "line1_current": data[6],
            "line2_current": data[7],
            "line3_current": data[8],
            "temperature": data[9],
        })

    return logs   

def get_alarms_history(id, rated_voltage, rated_current, max_temperature, limit):
    alarms_history = []

    result = metrics_repository.get_metrics_logs(id, limit)
    for data in result:
        result = [data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]]
        alarms = analyze_metrics(result, rated_voltage, rated_current, max_temperature)
        alarms_history.extend(alarms)

    return alarms_history

## Private Functions

def analyze_metrics(result, rated_voltage, rated_current, max_temperature):
    alarms_list = []

    # Over Voltage
    if alarms.check_over_voltage(result[2], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Phase 1 Over Voltage",
            "status": alarms.check_over_voltage(result[2], rated_voltage)
        })
    if alarms.check_over_voltage(result[3], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Phase 2 Over Voltage",
            "status": alarms.check_over_voltage(result[3], rated_voltage)
        })
    if alarms.check_over_voltage(result[4], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Phase 3 Over Voltage",
            "status": alarms.check_over_voltage(result[4], rated_voltage)
        })

    # Under Voltage
    if alarms.check_under_voltage(result[2], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Phase 1 Under Voltage",
            "status": alarms.check_under_voltage(result[2], rated_voltage)
        })
    if alarms.check_under_voltage(result[3], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Phase 2 Under Voltage",
            "status": alarms.check_under_voltage(result[3], rated_voltage)
        })
    if alarms.check_under_voltage(result[4], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Phase 3 Under Voltage",
            "status": alarms.check_under_voltage(result[4], rated_voltage)
        })

    # Short Circuit
    if alarms.check_short_circuit(result[5], rated_current) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Line 1 Short Circuit",
            "status": alarms.check_short_circuit(result[5], rated_current)
        })
    if alarms.check_short_circuit(result[6], rated_current) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Line 2 Short Circuit",
            "status": alarms.check_short_circuit(result[6], rated_current)
        })
    if alarms.check_short_circuit(result[7], rated_current) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Line 3 Short Circuit",
            "status": alarms.check_short_circuit(result[7], rated_current)
        })
    
    # No Power
    if alarms.check_no_power(result[2], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Line 1 No Power",
            "status": alarms.check_no_power(result[2], rated_voltage)
        })
    if alarms.check_no_power(result[3], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Line 2 No Power",
            "status": alarms.check_no_power(result[3], rated_voltage)
        })
    if alarms.check_no_power(result[4], rated_voltage) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Line 3 No Power",
            "status": alarms.check_no_power(result[4], rated_voltage)
        })

    # Phase Loss
    phase_loss_alarm = "Overcurrent due to Phase Loss"
    if alarms.check_phase_loss(result[5], rated_current) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": phase_loss_alarm,
            "status": alarms.check_phase_loss(result[5], rated_current)
        })
    elif alarms.check_phase_loss(result[6], rated_current) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": phase_loss_alarm,
            "status": alarms.check_phase_loss(result[6], rated_current)
        })
    elif alarms.check_phase_loss(result[7], rated_current) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": phase_loss_alarm,
            "status": alarms.check_phase_loss(result[7], rated_current)
        })

    # Temperature
    if alarms.check_temperature(result[8], max_temperature) != severity.NORMAL:
        alarms_list.append({
            "timestamp": result[0],
            "alarm": "Overheating",
            "status": alarms.check_temperature(result[8], max_temperature)
        })

    return alarms_list

def generate_trend(result, trend_names, limit):
    recorded_timestamps = generate_timestamps(limit)
    raw = []
    trend = []
    timestamps = []

    for trend_name in trend_names:
        trend.append({
            "name": trend_name,
            "data": []
        })
    trend_sets = len(trend)

    
    for data in result:
        if trend_sets >= 2:
            raw.insert(0, [convert_timestamp(data[0]), data[1], data[2], data[3]])
        else:
            raw.insert(0, [convert_timestamp(data[0]), data[1]])

    if len(result) == 0:
        timestamps.extend(recorded_timestamps)
        trend[0]["data"].extend([0.00] * limit)
        if trend_sets >= 2:
            trend[1]["data"].extend([0.00] * limit)
            trend[2]["data"].extend([0.00] * limit)
    
    else:
        counter = 0
        rawLimit = len(raw)
        for timestamp in recorded_timestamps:
            if timestamp == raw[counter][0]:
                data = raw[counter]
                timestamps.append(data[0])
                trend[0]["data"].append(data[1])
                if trend_sets >= 2:
                    trend[1]["data"].append(data[2])
                    trend[2]["data"].append(data[3])
                if (counter) <= rawLimit :
                    counter += 1
            else:
                timestamps.insert(0, timestamp)
                trend[0]["data"].append(0.00)
                if trend_sets >= 2:
                    trend[1]["data"].append(0.00)
                    trend[2]["data"].append(0.00)
 
    return {
        "trend": trend,
        "timestamps": timestamps
    }

