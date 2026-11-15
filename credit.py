def calculate_risk(income, debt):
    if income <= 0:
        return -1

    ratio = debt / income

    if ratio > 0.6:
        return "HIGH"
    elif ratio > 0.3:
        return "MEDIUM"
    else:
        return "LOW"