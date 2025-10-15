from typing import Union, Any


class Employee:
    # PRIVATE Name : STRING
    # PRIVATE Age : INTEGER
    def __init__(self, nameP, ageP):
        self.__Name = nameP
        self.__Age = ageP

    def getName(self):
        return self.__Name


class FullTime(Employee):
    # PRIVATE MonthlyRate : INTEGER
    def __init__(self, nameP, ageP, monthlyRateP):
        super().__init__(nameP, ageP)
        self.__MonthlyRate = monthlyRateP

    def YearlySalary(self):
        temp = self.__MonthlyRate * 12
        return temp


class PartTime(Employee):
    # PRIVATE HourlyRate : INTEGER
    def __init__(self, nameP, ageP, hourlyRateP):
        super().__init__(nameP, ageP)
        self.__HourlyRate = hourlyRateP

    def DailyWage(self, HoursWorked):
        temp = HoursWorked * self.__HourlyRate
        return temp


worker = PartTime("aijaz", 50, 20)
permanent_worker = FullTime("ali", 35, 5000)
print(permanent_worker.getName())
print(permanent_worker.YearlySalary())
print(worker.DailyWage(6))
print(worker.getName())