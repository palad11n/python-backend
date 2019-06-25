#!/usr/bin/env python
from random import randint


class Car(object):

    def __init__(self, name, max_speed=0, drag_coef=0., time_to_max=0):
        self._check(max_speed, drag_coef, time_to_max)
        self.name = name
        self.max_speed = max_speed
        self.drag_coef = drag_coef
        self.time_to_max = time_to_max

    def _check(self, max_speed, drag_coef, time_to_max):
        if not isinstance(max_speed, int):
            raise TypeError("Max speed must be set to an integer")
        if not isinstance(drag_coef, float):
            raise TypeError("Drag coef must be set to an float")
        if not isinstance(time_to_max, int):
            raise TypeError("Time to max must be set to an integer")

    def printCar(self):
        print('Name: {0}, max_speed: {1}, drag_coef: {2}, time_to_max: {3} '.format(
            self.name, self.max_speed, self.drag_coef, self.time_to_max))


class Weather(object):

    def __init__(self, _wind_speed=0):
        self._check(_wind_speed)
        self.wind_speed = _wind_speed

    def _check(self, _wind_speed):
        if not isinstance(_wind_speed, int):
            raise TypeError("Wind speed must be set to an integer")


class Rush(object):
    _count = 0

    def __init__(self, distance):
        self._check(distance)
        self.distance = distance

    def _check(self, dist):
        if not isinstance(dist, int):
            raise TypeError("Wind speed must be set to an integer")

    def __new__(cls, *args, **kwargs):
        if cls._count == 0:
            Rush._count += 1
            return object.__new__(cls)

    def start(self, competitors, weather):
        for car in competitors:
            competitor_time = 0

            for distance in range(self.distance):
                _wind_speed = randint(0, weather.wind_speed)

                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / car.time_to_max) * car.max_speed
                    if _speed > _wind_speed:
                        _speed -= (car.drag_coef * _wind_speed)

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (car.name, competitor_time))


competitors = (
    Car('ferrary', 340, 0.324, 26),
    Car('bugatti', 407, 0.39, 32),
    Car('toyota', 180, 0.25, 40),
    Car('lada', 180, 0.32, 56),
    Car('sx4', 180, 0.33, 44)
)
rush = Rush(10000).start(competitors, Weather(20))