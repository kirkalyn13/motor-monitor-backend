import utilities.severities as severity

NULL_LATEST_METRICS = {
    "line1Voltage": {
        "value": 0.0,
        "status": severity.NULL
    },
    "line2Voltage": {
        "value": 0.0,
        "status": severity.NULL
    },
    "line3Voltage": {
        "value": 0.0,
        "status": severity.NULL
    },
    "line1Current": {
        "value": 0.0,
        "status": severity.NULL
    },
    "line2Current": {
        "value": 0.0,
        "status": severity.NULL
    },
    "line3Current": {
        "value": 0.0,
        "status": severity.NULL
    },
    "temperature": {
        "value": 0.0,
        "status": severity.NULL
    }
}

NULL_METRICS_SUMMARY = { "summary": [ 0, 0, 0 ] }

NULL_ALARMS_LIST = [
    {
    "alarm": "Monitoring Device is OFF",
    "status": severity.NULL
    },
]