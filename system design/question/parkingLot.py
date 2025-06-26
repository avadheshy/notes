# from typing import List
# from abc import ABC
# from enum import Enum


# class VehicleType(Enum):
#     CAR = 1
#     MOTORCYCLE = 2
#     TRUCK = 3


# class Vehicle(ABC):
#     def __init__(self, license_plate: str, vehicle_type: VehicleType):
#         self.license_plate = license_plate
#         self.type = vehicle_type

#     def get_type(self) -> VehicleType:
#         return self.type


# class Truck(Vehicle):
#     def __init__(self, license_plate: str):
#         super().__init__(license_plate, VehicleType.TRUCK)


# class Car(Vehicle):
#     def __init__(self, license_plate: str):
#         super().__init__(license_plate, VehicleType.CAR)


# class Motorcycle(Vehicle):
#     def __init__(self, license_plate: str):
#         super().__init__(license_plate, VehicleType.MOTORCYCLE)


# class ParkingSpot:
#     def __init__(self, spot_number: int, vehicle_type: VehicleType):
#         self.spot_number = spot_number
#         self.vehicle_type = vehicle_type
#         self.parked_vehicle: Vehicle = None

#     def is_available(self) -> bool:
#         return self.parked_vehicle is None

#     def park_vehicle(self, vehicle: Vehicle) -> None:
#         if self.is_available() and vehicle.get_type() == self.vehicle_type:
#             self.parked_vehicle = vehicle
#         else:
#             raise ValueError(f"Spot {self.spot_number} is not suitable or already occupied.")

#     def unpark_vehicle(self) -> None:
#         if self.parked_vehicle:
#             self.parked_vehicle = None
#         else:
#             raise ValueError(f"Spot {self.spot_number} is already empty.")

#     def get_spot_number(self) -> int:
#         return self.spot_number


# class Level:
#     def __init__(self, floor: int, spot_types: List[VehicleType]):
#         self.floor = floor
#         self.parking_spots: List[ParkingSpot] = [
#             ParkingSpot(i, vehicle_type) for i, vehicle_type in enumerate(spot_types)
#         ]

#     def park_vehicle(self, vehicle: Vehicle) -> bool:
#         for spot in self.parking_spots:
#             if spot.is_available() and spot.vehicle_type == vehicle.get_type():
#                 spot.park_vehicle(vehicle)
#                 return True
#         return False

#     def unpark_vehicle(self, vehicle: Vehicle) -> bool:
#         for spot in self.parking_spots:
#             if not spot.is_available() and spot.parked_vehicle == vehicle:
#                 spot.unpark_vehicle()
#                 return True
#         return False

#     def display_availability(self) -> None:
#         print(f"Level {self.floor} Availability:")
#         for spot in self.parking_spots:
#             status = "Available" if spot.is_available() else f"Occupied by {spot.parked_vehicle.license_plate}"
#             print(f"  Spot {spot.get_spot_number()}: {status}")


# class ParkingLot:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self):
#         if not hasattr(self, "levels"):
#             self.levels: List[Level] = []

#     def add_level(self, level: Level) -> None:
#         self.levels.append(level)

#     def park_vehicle(self, vehicle: Vehicle) -> bool:
#         for level in self.levels:
#             if level.park_vehicle(vehicle):
#                 return True
#         return False

#     def unpark_vehicle(self, vehicle: Vehicle) -> bool:
#         for level in self.levels:
#             if level.unpark_vehicle(vehicle):
#                 return True
#         return False

#     def display_availability(self) -> None:
#         for level in self.levels:
#             level.display_availability()


# class ParkingLotDemo:
#     @staticmethod
#     def run():
#         parking_lot = ParkingLot()

#         # Define mixed levels with different vehicle types
#         level_1_spots = [VehicleType.CAR] * 70 + [VehicleType.MOTORCYCLE] * 20 + [VehicleType.TRUCK] * 10
#         level_2_spots = [VehicleType.CAR] * 50 + [VehicleType.MOTORCYCLE] * 30

#         parking_lot.add_level(Level(1, level_1_spots))
#         parking_lot.add_level(Level(2, level_2_spots))

#         # Create vehicles
#         car = Car("ABC123")
#         truck = Truck("XYZ789")
#         motorcycle = Motorcycle("M1234")

#         # Park vehicles
#         assert parking_lot.park_vehicle(car), "Failed to park car"
#         assert parking_lot.park_vehicle(truck), "Failed to park truck"
#         assert parking_lot.park_vehicle(motorcycle), "Failed to park motorcycle"

#         # Display availability
#         print("\nInitial Parking Lot Availability:")
#         parking_lot.display_availability()

#         # Unpark a vehicle
#         parking_lot.unpark_vehicle(motorcycle)

#         # Display updated availability
#         print("\nUpdated Parking Lot Availability after Unparking Motorcycle:")
#         parking_lot.display_availability()


# if __name__ == "__main__":
#     ParkingLotDemo.run()
"""
Designing a Parking Lot System
Requirements
The parking lot should have multiple levels, each level with a certain number of parking spots.
The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
Each parking spot should be able to accommodate a specific type of vehicle.
The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
The system should track the availability of parking spots and provide real-time information to customers.
The system should handle multiple entry and exit points and support concurrent access.
"""

from enum import Enum
class VehicleType(Enum):
    MotorCycle=1
    Car=2
    Truck=3
class Vehicle():
    def __init__(self,number_plate,vehicle_type):
        self.number_plate=number_plate
        self.vehicle_type=vehicle_type
class MotorByke(Vehicle):
    def __init__(self,number_pate,vehicle_type):
        super(MotorByke).__init__(number_pate,vehicle_type)

class Car:
    def __init__(self,number_pate,vehicle_type):
        super(MotorByke).__init__(number_pate,vehicle_type)

class Truck:
    def __init__(self,number_pate,vehicle_type):
        super(MotorByke).__init__(number_pate,vehicle_type)

class ParkingSpot():
    def __init__(self,vehicle_type):
        self.vehicle_type=vehicle_type
        self.vehicle:VehicleType=None
        
    def is_full(self,vehicle_type):
        return self.vehicle is None
    
    def park(self,vehicle):
        if self.is_full:
            return "parking lot is already full"
        elif self.vehicle!=vehicle.vehicle_type:
            return "parki lot is not suitable for this type of vehicle"
        self.vehicle=vehicle
        
    def un_park(self):
        self.vehicle=None

class ParkingLot():
    def __init__(self,park_locacation):
        self.level=len(park_locacation)
        self.parking_location=[[] for _ in range(self.level)]
        for i in range(self.level):
            for j in range(len(park_locacation[i])):
                self.parking_location.append(ParkingSpot(park_locacation[i][j]))
        
    def get_available_spot(self,vehicle_type):
        for i in range(self.level):
            for j in range(len(self.parking_location)):
                if self.parking_location[i][j].ParkingSpot.vehicle_type==vehicle_type and self.parking_location[i][j].ParkingSpot.vehicle is None:
                    print(f"parking number is {j} and parking level is {i}")
    
    def check_empty_spot(self,level,spot_number):
        return self.parking_location[level][spot_number].ParkingSpot is None
    
    def park_vehicle(self,level,spot_number,vehicle,vehicle_type):
        if not self.check_empty_spot(level,spot_number):
            raise ValueError('Spot is not free')
        elif self.parking_location[level][spot_number].ParkingSpot.vehicle_type!=vehicle_type:
            raise ValueError("vehicle type is not matching at that spot")
        self.parking_location[level][spot_number].ParkingSpot.vehicle=vehicle
    
    def unpark_vehicle(self,level,spot_number,vehicle):
        if self.parking_location[level][spot_number].ParkingSpot.vehicle is None:
            raise ValueError("spot is all ready empty")
        self.parking_location[level][spot_number].ParkingSpot.vehicle =None
        
if __name__=="__main__":
    arr=[[[VehicleType.MotorCycle]*10+[VehicleType.Car]*20+[VehicleType.Truck]*20],
         [[VehicleType.MotorCycle]*20+[VehicleType.Car]*20+[VehicleType.Truck]*10],
         [[VehicleType.MotorCycle]*30+[VehicleType.Car]*10+[VehicleType.Truck]*10]
         ]
    parking_lot=ParkingLot(arr)
        
        
        
        
        
        