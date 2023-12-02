import repositories.metrics_repository as metrics_repository
import calculators.alarms as alarms
from calculators.status import get_status
from utilities.time import convert_timestamp

def get_latest_metrics(id, rated_voltage, rated_current, max_temperature):
    result = metrics_repository.get_latest_metrics(id)[0]
    latest_metrics = {
        "timestamp": result[0],
        "unitID": result[1],
        "line1Voltage": {
            "value": result[2],
            "status": get_status(result[2], rated_voltage)
        },
        "line2Voltage": {
            "value": result[3],
            "status": get_status(result[3], rated_voltage)
        },
        "line3Voltage": {
            "value": result[4],
            "status": get_status(result[4], rated_voltage)
        },
        "line1Current": {
            "value": result[5],
            "status": get_status(result[5], rated_current)
        },
        "line2Current": {
            "value": result[6],
            "status": get_status(result[6], rated_current)
        },
        "line3Current": {
            "value": result[7],
            "status": get_status(result[7], rated_current)
        },
        "temperature": {
            "value": result[8],
            "status": get_status(result[8], max_temperature)
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
            get_status(result[2], rated_voltage),
            get_status(result[3], rated_voltage),
            get_status(result[4], rated_voltage),
            get_status(result[5], rated_current),
            get_status(result[6], rated_current),
            get_status(result[7], rated_current),
            get_status(result[8], max_temperature)
    ]

    normal_count = 0
    warning_count = 0
    critical_count = 0
    
    for status in metrics_status:
        if status == "normal":
            normal_count += 1
        elif status == "warning":
            warning_count += 1
        elif status == "critical":
            critical_count += 1

    return {
        "summary": [ normal_count, warning_count, critical_count ]
    }

def get_alarms(id, rated_voltage, rated_current, max_temperature):
    result = metrics_repository.get_latest_metrics(id)[0]
    alarms_list = []

    # Over Voltage
    if alarms.check_over_voltage(result[2], rated_voltage) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Line 1 Over Voltage",
            "status": alarms.check_over_voltage(result[2], rated_voltage)
        })
    if alarms.check_over_voltage(result[3], rated_voltage) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Line 2 Over Voltage",
            "status": alarms.check_over_voltage(result[3], rated_voltage)
        })
    if alarms.check_over_voltage(result[4], rated_voltage) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Line 3 Over Voltage",
            "status": alarms.check_over_voltage(result[4], rated_voltage)
        })

    # Under Voltage
    if alarms.check_under_voltage(result[2], rated_voltage) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Line 1 Under Voltage",
            "status": alarms.check_under_voltage(result[2], rated_voltage)
        })
    if alarms.check_under_voltage(result[3], rated_voltage) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Line 2 Under Voltage",
            "status": alarms.check_under_voltage(result[3], rated_voltage)
        })
    if alarms.check_under_voltage(result[4], rated_voltage) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Line 3 Under Voltage",
            "status": alarms.check_under_voltage(result[4], rated_voltage)
        })

    # Short Circuit
    if alarms.check_short_circuit(result[5], rated_current) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Line 1 Short Circuit",
            "status": alarms.check_short_circuit(result[5], rated_current)
        })
    if alarms.check_short_circuit(result[6], rated_current) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Line 2 Short Circuit",
            "status": alarms.check_short_circuit(result[6], rated_current)
        })
    if alarms.check_short_circuit(result[7], rated_current) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Line 3 Short Circuit",
            "status": alarms.check_short_circuit(result[7], rated_current)
        })

    # Temperature
    if alarms.check_temperature(result[8], max_temperature) != alarms.NORMAL:
        alarms_list.append({
            "alarm": "Overheating",
            "status": alarms.check_temperature(result[8], max_temperature)
        })

    return alarms_list
