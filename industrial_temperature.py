def trigger_alarm(temperatures, threshold=80):
    alarms = []

    for sensor, temp in temperatures.items():
        if temp > threshold:
            alarms.append(sensor)

    return alarms