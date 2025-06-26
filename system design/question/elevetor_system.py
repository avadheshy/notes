"""
Designing an Elevator System
Requirements
The elevator system should consist of multiple elevators serving multiple floors.
Each elevator should have a capacity limit and should not exceed it.
Users should be able to request an elevator from any floor and select a destination floor.
The elevator system should efficiently handle user requests and optimize the movement of elevators to minimize waiting time.
The system should prioritize requests based on the direction of travel and the proximity of the elevators to the requested floor.
The elevators should be able to handle multiple requests concurrently and process them in an optimal order.
The system should ensure thread safety and prevent race conditions when multiple threads interact with the elevators.
"""
from enum import Enum
from collections import deque


class Direction(Enum):
    UP = 'up'
    Down = 'down'


class Request:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.direction = Direction.UP.value if source < destination else Direction.Down.value
        self.weight = weight
        self.completed = False


class Elevetor:
    def __init__(self, number, limit):
        self.number = number
        self.state = None
        self.direction: Direction = None
        self.limit = limit


class ElevetorSystem():
    def __init__(self, floor, n):
        self.floor = floor
        self.elevetor = [Elevetor() for i in range(n)]
        self.requests: Request = deque()

    def request_lift(self, source, destination, weight):
        self.requests.append(Request(source, destination, weight))

    def solve_request(self):
        while len(self.requests):
            pass
    def remove_completed_request(self):
        self.req:Request=deque()
        for i in self.requests:
            if not i.completed:
                self.que.append(i)
        self.requests=self.req
