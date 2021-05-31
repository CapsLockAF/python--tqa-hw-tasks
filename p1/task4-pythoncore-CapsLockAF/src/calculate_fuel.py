def calculate_fuel(distance):
    # Type your code
    f = distance * 10
    return f < 100 and 100 or f if distance > 0 else False
