import utilities.severities as severity

def get_status(value, limit):
    if value >= limit:
        return severity.CRITICAL
    elif value == 0:
        return severity.CRITICAL
    elif value >= limit:
        return severity.WARNING
    else:
        return severity.NORMAL