# Write your code here!
def temp_and_color(data):
    temp = data["temp"] if "temp" in data else None
    color = data["color"] if "color" in data else None
    return temp, color