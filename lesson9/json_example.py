#
import json


class Car():
    def __init__(self, color, speed, *args, **kwargs):
        self.color = color
        self.speed = speed


focus = Car('red', 220)
fiesta = Car('black', 170)

focus_to_json = {'color': focus.color, 'speed': focus.speed}

to_json = json.dumps(focus_to_json)
print(to_json)
to_dump = json.loads(to_json)
print(to_dump)
