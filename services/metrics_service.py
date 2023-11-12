import repository.metrics_repository as metrics_repository

def get_latest_metrics(id):
    result = metrics_repository.get_latest_metrics(id)[0]
    latest_metrics = {
        "timestamp": result[1],
        "unitID": result[2],
        "line1Voltage": result[3],
        "line2Voltage": result[4],
        "line3Voltage": result[5],
        "line1Current": result[6],
        "line2Current": result[7],
        "line3Current": result[8],
        "temperature": result[9],
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