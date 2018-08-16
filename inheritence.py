class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        calculate = 0
        result = ""
        for i in self.scores:
            calculate += i
        ans = calculate//len(self.scores)
        if ans < 40:
            result = "T"
        elif ans >= 40 and ans < 55:
            result = "D"
        elif ans >= 55 and ans < 70:
            result = "P"
        elif ans >= 70 and ans < 80:
            result = "A"
        elif ans >= 80 and ans < 90:
            result = "E"
        elif ans >= 90 and ans <= 100:
            result = "O"
        print("Grade:", result)


firstName, lastName, inNumber = input().split()
n = int(input())
scores = list(map(int, input().split()))
student = Student(firstName, lastName, inNumber, scores)
student.printPerson()
student.calculate()
