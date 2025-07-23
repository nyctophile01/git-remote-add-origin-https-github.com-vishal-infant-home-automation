import random
def get_temperature():
    return round(random.uniform(20.0, 30.0), 1)
def detect_sound():
    return random.choice([True, False])
def get_light_status():
    return random.choice(["ON", "OFF"])