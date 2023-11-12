import repository.metrics_repository as metrics_repository
from calculators.status import get_status

def get_latest_metrics(id, rated_voltage, rated_current, max_temperature):
    result = metrics_repository.get_latest_metrics(id)[0]
    latest_metrics = {
        "timestamp": result[1],
        "unitID": result[2],
        "metrics": {
            "line1Voltage": result[3],
            "line2Voltage": result[4],
            "line3Voltage": result[5],
            "line1Current": result[6],
            "line2Current": result[7],
            "line3Current": result[8],
            "temperature": result[9],
        },
        "status" : {
            "line1Voltage": get_status(result[3], rated_voltage),
            "line2Voltage": get_status(result[4], rated_voltage),
            "line3Voltage": get_status(result[5], rated_voltage),
            "line1Current": get_status(result[6], rated_current),
            "line2Current": get_status(result[7], rated_current),
            "line3Current": get_status(result[8], rated_current),
            "temperature": get_status(result[9], max_temperature),
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

    result = metrics_repository.get_voltage_trend(id)
    for data in result:
        voltage_trend[0]["data"].append(data[0])
        voltage_trend[1]["data"].append(data[1])
        voltage_trend[2]["data"].append(data[2])

    return voltage_trend

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

    result = metrics_repository.get_current_trend(id)
    for data in result:
        current_trend[0]["data"].append(data[0])
        current_trend[1]["data"].append(data[1])
        current_trend[2]["data"].append(data[2])

    return current_trend

def get_temperature_trend(id):
    temperature_trend = [{
        "name": "Temperature",
        "data": []
    }]

    result = metrics_repository.get_current_trend(id)
    for data in result:
        temperature_trend[0]["data"].append(data[0])

    return temperature_trend