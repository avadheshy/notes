"""
The traffic signal system should control the flow of traffic at an intersection with multiple roads.
The system should support different types of signals, such as red, yellow, and green.
The duration of each signal should be configurable and adjustable based on traffic conditions.
The system should handle the transition between signals smoothly, ensuring safe and efficient traffic flow.
The system should be able to detect and handle emergency situations, such as an ambulance or fire truck approaching the intersection.
The system should be scalable and extensible to support additional features and functionality.
"""
from enum import Enum
from abc import ABC, abstractmethod
from typing import Dict, List
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor


class Direction(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


class LightColor(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"


class TrafficObserver(ABC):

    @abstractmethod
    def update(self, intersection_id, direction, color):
        pass


class CentralMonitor(TrafficObserver):

    def update(self, intersection_id, direction, color):
        print(
            f"[MONITOR] Intersection={intersection_id} "
            f"Direction={direction.value} "
            f"Color={color.value}"
        )


class SignalState(ABC):

    @abstractmethod
    def handle(self, light):
        pass


class RedState(SignalState):

    def handle(self, light):
        light.set_color(LightColor.RED)
        light.next_state = GreenState()


class GreenState(SignalState):

    def handle(self, light):
        light.set_color(LightColor.GREEN)
        light.next_state = YellowState()


class YellowState(SignalState):

    def handle(self, light):
        light.set_color(LightColor.YELLOW)
        light.next_state = RedState()


class TrafficLight:

    def __init__(self, intersection_id, direction):

        self.intersection_id = intersection_id
        self.direction = direction

        self.current_color = None
        self.current_state = RedState()
        self.next_state = None

        self.observers = []

        self.current_state.handle(self)

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(
                self.intersection_id,
                self.direction,
                self.current_color
            )

    def set_color(self, color):

        if self.current_color != color:
            self.current_color = color
            self.notify()

    def start_green(self):
        self.current_state = GreenState()
        self.current_state.handle(self)

    def transition(self):
        self.current_state = self.next_state
        self.current_state.handle(self)


class TrafficSensor:

    def get_vehicle_count(self, direction):
        return random.randint(10, 100)


class EmergencyVehicleDetector:

    def detect(self):
        if random.randint(1, 100) <= 5:
            return random.choice(list(Direction))

        return None


class IntersectionState(ABC):

    @abstractmethod
    def handle(self, controller):
        pass


class NorthSouthGreenState(IntersectionState):

    def handle(self, controller):

        controller.activate_green(
            [Direction.NORTH, Direction.SOUTH],
            [Direction.EAST, Direction.WEST]
        )

        controller.current_state = EastWestGreenState()


class EastWestGreenState(IntersectionState):

    def handle(self, controller):

        controller.activate_green(
            [Direction.EAST, Direction.WEST],
            [Direction.NORTH, Direction.SOUTH]
        )

        controller.current_state = NorthSouthGreenState()


class EmergencyState(IntersectionState):

    def __init__(self, direction):
        self.direction = direction

    def handle(self, controller):

        print(
            f"\n***** EMERGENCY VEHICLE FROM "
            f"{self.direction.value} *****"
        )

        for light in controller.traffic_lights.values():
            light.set_color(LightColor.RED)

        controller.get_light(
            self.direction
        ).set_color(
            LightColor.GREEN
        )

        time.sleep(10)

        controller.current_state = NorthSouthGreenState()


class IntersectionController:

    def __init__(
            self,
            intersection_id,
            lights,
            green_duration,
            yellow_duration
    ):

        self.intersection_id = intersection_id

        self.traffic_lights = lights

        self.green_duration = green_duration
        self.yellow_duration = yellow_duration

        self.sensor = TrafficSensor()
        self.emergency_detector = EmergencyVehicleDetector()

        self.current_state = NorthSouthGreenState()

        self.running = True

    def get_light(self, direction):
        return self.traffic_lights[direction]

    def get_dynamic_green_duration(self, direction):

        count = self.sensor.get_vehicle_count(direction)

        if count > 70:
            return 10

        if count > 40:
            return 7

        return 5

    def activate_green(
            self,
            green_directions,
            red_directions
    ):

        print(
            f"\nIntersection "
            f"{self.intersection_id}"
        )

        for direction in red_directions:
            self.get_light(direction).set_color(
                LightColor.RED
            )

        for direction in green_directions:
            self.get_light(direction).start_green()

        duration = self.get_dynamic_green_duration(
            green_directions[0]
        )

        time.sleep(duration)

        for direction in green_directions:
            self.get_light(direction).transition()

        time.sleep(
            self.yellow_duration
        )

        for direction in green_directions:
            self.get_light(direction).transition()

    def run(self):

        while self.running:

            emergency_direction = (
                self.emergency_detector.detect()
            )

            if emergency_direction:

                EmergencyState(
                    emergency_direction
                ).handle(self)

                continue

            self.current_state.handle(self)

    def stop(self):
        self.running = False

    class Builder:

        def __init__(self, intersection_id):

            self.intersection_id = intersection_id

            self.green_duration = 5
            self.yellow_duration = 2

            self.observers = []

        def with_durations(
                self,
                green,
                yellow
        ):

            self.green_duration = green
            self.yellow_duration = yellow

            return self

        def add_observer(self, observer):

            self.observers.append(observer)

            return self

        def build(self):

            lights = {}

            for direction in Direction:

                light = TrafficLight(
                    self.intersection_id,
                    direction
                )

                for observer in self.observers:
                    light.add_observer(observer)

                lights[direction] = light

            return IntersectionController(
                self.intersection_id,
                lights,
                self.green_duration,
                self.yellow_duration
            )


class TrafficControlSystem:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):

        if cls._instance is None:

            with cls._lock:

                if cls._instance is None:
                    cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if not hasattr(self, "intersections"):

            self.intersections = []
            self.executor = None

    def add_intersection(
            self,
            intersection_id,
            green_duration=5,
            yellow_duration=2
    ):

        intersection = (
            IntersectionController.Builder(
                intersection_id
            )
            .with_durations(
                green_duration,
                yellow_duration
            )
            .add_observer(
                CentralMonitor()
            )
            .build()
        )

        self.intersections.append(
            intersection
        )

    def start(self):

        self.executor = ThreadPoolExecutor(
            max_workers=len(self.intersections)
        )

        for intersection in self.intersections:
            self.executor.submit(
                intersection.run
            )

    def stop(self):

        for intersection in self.intersections:
            intersection.stop()

        if self.executor:
            self.executor.shutdown(
                wait=True
            )


if __name__ == "__main__":

    system = TrafficControlSystem()

    system.add_intersection(
        intersection_id=1,
        green_duration=5,
        yellow_duration=2
    )

    system.add_intersection(
        intersection_id=2,
        green_duration=5,
        yellow_duration=2
    )

    system.start()

    try:
        time.sleep(60)

    except KeyboardInterrupt:
        pass

    finally:
        system.stop()
