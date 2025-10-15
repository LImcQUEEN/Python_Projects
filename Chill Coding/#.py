class Teachers:
    def __init__(self, NameP, ClassP, SectionP):
        self.__Name = NameP
        self.__Class = ClassP
        self.__Salary = 0
        self.__Section = SectionP

    def GetName(self):
        return self.__Name

    def GetClass(self):
        return self.__Class

    def GetSection(self):
        return self.__Section

    def SetSalary(self, rank):
        if rank == "Senior":
            self.__Salary = 10000
        elif rank == "Junior":
            self.__Salary = 7500
        elif rank == "Intern":
            self.__Salary = 5000

    def GetSalary(self):
        return self.__Salary


class Student(Teachers):
    def __init__(self, NameP, ClassP, SectionP):
        super().__init__(NameP, ClassP, SectionP)
        self.__Grade = "U"

    def GetName(self):
        super().GetName()

    def GetClass(self):
        super().GetClass()

    def GetSection(self):
        super().GetSection()

    def SetGrade(self, Marks):
        if Marks >= 90:
            self.__Grade = "A*"
        elif Marks >= 80:
            self.__Grade = "A"
        elif Marks >= 70:
            self.__Grade = "B"
        elif Marks >= 60:
            self.__Grade = "C"
        elif Marks >= 50:
            self.__Grade = "D"
        else:
            self.__Grade = "Fail"

