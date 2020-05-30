class Car:
    SINCE = 1990

    def __init__(self, color, style, max_speed):
        self.color = color
        self.style = style
        self.max_speed = max_speed
        self._current_speed = 0
        # print('__init__ called')

    def move(self, speed):
        # self._current_speed = speed
        self.current_speed = speed
        print(f'moving car at {speed} kmh')

    @property
    def current_speed(self):
        print('getter called')
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        print('setter called')
        if value <= self.max_speed:
            self._current_speed = value


car1 = Car('blue', 'SUV', 230)
car1.move(200)
print(car1.current_speed)
