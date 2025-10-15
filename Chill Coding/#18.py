class Car:
    def drive(self):
        print("Driving car")


class SportCar(Car):
    def drive(self):
        super().drive()
        print("Driving A car")


my_car = SportCar()
my_car.drive()