def get_status(value, limit):
    if value > limit:
        return "critical"
    elif value == 0:
        return "critical"
    elif value > (limit*0.9):
        return "warning"
    else:
        return "normal"