
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
"""
Parking Lot System
"""

from enum import Enum
from threading import Lock
class VehicleType(Enum):
    MotorCycle = 1
    Car = 2
    Truck = 3


# ─── Vehicles ────────────────────────────────────────────────────────────────

class Vehicle:
    def __init__(self, number_plate: str, vehicle_type: VehicleType):
        self.number_plate = number_plate
        self.vehicle_type = vehicle_type

    def __repr__(self):
        return f"{self.__class__.__name__}({self.number_plate})"


class MotorCycle(Vehicle):               
    def __init__(self, number_plate: str):
        super().__init__(number_plate, VehicleType.MotorCycle)   


class Car(Vehicle):                     
    def __init__(self, number_plate: str):
        super().__init__(number_plate, VehicleType.Car)


class Truck(Vehicle):                    
    def __init__(self, number_plate: str):
        super().__init__(number_plate, VehicleType.Truck)




class ParkingSpot:
    def __init__(self, spot_id: int, vehicle_type: VehicleType):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.vehicle: Vehicle | None = None

    def is_available(self) -> bool:
        return self.vehicle is None        

    def park(self, vehicle: Vehicle) -> bool:
        if not self.is_available():
            print(f"  [Spot {self.spot_id}] Already occupied by {self.vehicle}")
            return False
        if self.vehicle_type != vehicle.vehicle_type:    
            print(f"  [Spot {self.spot_id}] Type mismatch: spot={self.vehicle_type.name}, vehicle={vehicle.vehicle_type.name}")
            return False
        self.vehicle = vehicle
        return True

    def un_park(self) -> Vehicle | None:
        if self.is_available():
            print(f"  [Spot {self.spot_id}] Already empty")
            return None
        removed = self.vehicle
        self.vehicle = None
        return removed

    def __repr__(self):
        status = str(self.vehicle) if self.vehicle else "empty"
        return f"Spot({self.spot_id}, {self.vehicle_type.name}, {status})"


# ─── ParkingLot ──────────────────────────────────────────────────────────────

class ParkingLot:
    """
    park_config: list of levels, each level is a flat list of VehicleType values.
    Example: [[VehicleType.Car]*3, [VehicleType.MotorCycle]*5]
    """

    def __init__(self, park_config: list[list[VehicleType]]):
        self._lock = Lock()                         
        self.num_levels = len(park_config)

        self.parking_location: list[list[ParkingSpot]] = []
        spot_id = 0
        for level_spots in park_config:
            level: list[ParkingSpot] = []
            for v_type in level_spots:
                level.append(ParkingSpot(spot_id, v_type))
                spot_id += 1
            self.parking_location.append(level)

    # ── Queries ──────────────────────────────────────────────────────────────

    def get_available_spots(self, vehicle_type: VehicleType) -> list[tuple[int, int]]:
        """Return [(level, spot_index), ...] for every free compatible spot."""
        result = []
        for lvl, spots in enumerate(self.parking_location):
            for idx, spot in enumerate(spots):
            
                if spot.vehicle_type == vehicle_type and spot.is_available():
                    result.append((lvl, idx))
        return result

    def check_available(self, level: int, spot_index: int) -> bool:
        return self.parking_location[level][spot_index].is_available()

    def availability_summary(self) -> dict:
        summary = {}
        for v_type in VehicleType:
            summary[v_type.name] = len(self.get_available_spots(v_type))
        return summary

    # ── Operations ───────────────────────────────────────────────────────────

    def park_vehicle(self, vehicle: Vehicle, level: int = None, spot_index: int = None) -> tuple[int, int] | None:
        """
        Auto-assign if level/spot_index are omitted.
        Returns (level, spot_index) on success, None on failure.
        Thread-safe.
        """
        with self._lock:
            if level is None or spot_index is None:
                candidates = self.get_available_spots(vehicle.vehicle_type)
                if not candidates:
                    print(f"No available spot for {vehicle.vehicle_type.name}")
                    return None
                level, spot_index = candidates[0]

            spot = self.parking_location[level][spot_index]
            success = spot.park(vehicle)
            if success:
                print(f"  Parked {vehicle} → Level {level}, Spot {spot_index}")
                return (level, spot_index)
            return None

    def unpark_vehicle(self, level: int, spot_index: int) -> Vehicle | None:
        """Release a spot. Returns the vehicle that was parked, or None."""
        with self._lock:
            spot = self.parking_location[level][spot_index]
            vehicle = spot.un_park()
            if vehicle:
                print(f"  Unparked {vehicle} ← Level {level}, Spot {spot_index}")
            return vehicle

    def __repr__(self):
        lines = [f"ParkingLot ({self.num_levels} levels)"]
        for lvl, spots in enumerate(self.parking_location):
            occupied = sum(1 for s in spots if not s.is_available())
            lines.append(f"  Level {lvl}: {occupied}/{len(spots)} occupied")
        return "\n".join(lines)


# ─── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    
    config = [
        [VehicleType.MotorCycle] * 10 + [VehicleType.Car] * 20 + [VehicleType.Truck] * 20,
        [VehicleType.MotorCycle] * 20 + [VehicleType.Car] * 20 + [VehicleType.Truck] * 10,
        [VehicleType.MotorCycle] * 30 + [VehicleType.Car] * 10 + [VehicleType.Truck] * 10,
    ]

    lot = ParkingLot(config)
    print(lot)
    print("\nAvailability:", lot.availability_summary())

    print("\n--- Parking vehicles ---")
    bike1  = MotorCycle("MH01-AA-1234")
    car1   = Car("DL01-BB-5678")
    truck1 = Truck("UP01-CC-9012")
    car2   = Car("HR01-DD-3456")

    pos_bike  = lot.park_vehicle(bike1)
    pos_car1  = lot.park_vehicle(car1)
    pos_truck = lot.park_vehicle(truck1)
    pos_car2  = lot.park_vehicle(car2)

    print("\nAvailability after parking:", lot.availability_summary())

    print("\n--- Unparking car1 ---")
    if pos_car1:
        lot.unpark_vehicle(*pos_car1)

    print("\nAvailability after unpark:", lot.availability_summary())

    print("\n--- Specific spot query ---")
    spots = lot.get_available_spots(VehicleType.Truck)
    print(f"Free truck spots (first 3): {spots[:3]}")
        
        
        
        
        
        