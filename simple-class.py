class Car:
    SINCE = 1990

    def __init__(self, color, style, max_speed):
        self.color = color
        self.style = style
        self.max_speed = max_speed
        self.current_speed = 0
        print('__init__ called')

    def move(self, speed):
        self.current_speed = speed
        print(f'moving car at {speed} kmh')


car1 = Car('blue', 'SUV', 230)

