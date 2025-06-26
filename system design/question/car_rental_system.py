"""
Designing a Car Rental System
Requirements
The car rental system should allow customers to browse and reserve available cars for specific dates.
Each car should have details such as make, model, year, license plate number, and rental price per day.
Customers should be able to search for cars based on various criteria, such as car type, price range, and availability.
The system should handle reservations, including creating, modifying, and canceling reservations.
The system should keep track of the availability of cars and update their status accordingly.
The system should handle customer information, including name, contact details, and driver's license information.
The system should handle payment processing for reservations.
The system should be able to handle concurrent reservations and ensure data consistency.
"""


class Car:
    def __init__(self, made_year, model, licence_plate_number, cost_per_day,):
        self.made_year = made_year
        self.model = model
        self.licence_plate_number = licence_plate_number
        self.cost_per_day = cost_per_day
        self.available = True
        self.start_date = []
        self.end_date = []
        self.is_booked = False

    def book_car(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.is_booked = True

    def cancel_car(self):
        self.available = True
        self.start_date = None
        self.end_date = None
        self.is_booked = False

    def return_car(self):
        self.available = True
        self.start_date = None
        self.end_date = None
        self.is_booked = False


class Customer:
    def __init__(self, name, number, licence_number):
        self.name = name
        self.number = number
        self.licence_number = licence_number


class Rental:
    def __init__(self):
        self.cars = []
        self.book_list = []

    def add_car(self, made_year, model, licence_plate_number, cost_per_day):
        self.cars.append(
            Car(made_year, model, licence_plate_number, cost_per_day))

    def search_car(self, start_date, end_date, min_price=0, max_price=float('inf'), model=None):
        available_cars = []
        for car in self.cars:
            available = False
            if car.available:
                available = True
            else:
                check = True
                for i in range(len(start_date)):
                    if start_date <= start_date[i] <= end_date or start_date <= end_date[i] <= end_date:
                        check = False
                available = check
            if available:
                price = min_price <= car.cost_per_day <= max_price
                if model:
                    if car.model == model and price:
                        available_cars.append(car)
                elif price:
                    available_cars.append(car)
        if len(available_cars) == 0:
            print('no car is available')
        else:
            for car in available_cars:
                print(car.cost_per_day, car.medel)

    def book_car(self, start_date, end_date, model, user, price):
        car = None
        for c in self.cars:
            if c.model == model:
                car = c
                break
        if car is not None:
            car.availeble = False
            car.start_date.append(start_date)
            car.end_date.append(end_date)
            self.book_list.append({
                'user': user,
                'price': price,
                'model': model,
                "payment_completed": False
            })

    def release_car(self, user, model, start_date, end_date):
        car = None
        for c in self.cars:
            if c.model == model:
                car = c
                break
        if car is not None:
            if len(car.start_date) == 1:
                car.available = True
                car.start_date = []
                car.end_date = []
            else:
                car.start_date.remove(start_date)
                car.end_date.remove(end_date)

        for book in self.book_list:
            if book.model == model and book.user == user:
                book.payment_completed = True

    def cancle_car(self,model,start_date,end_date):
        car = None
        for c in self.cars:
            if c.model == model:
                car = c
                break
        if car is not None:
            if len(car.start_date) == 1:
                car.available = True
                car.start_date = []
                car.end_date = []
            else:
                car.start_date.remove(start_date)
                car.end_date.remove(end_date)
        