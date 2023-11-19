import repositories.metrics_repository as metrics_repository
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