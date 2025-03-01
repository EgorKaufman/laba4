class Student:
    name = 'Egor'
    surname = 'Doynikov'
    
    def show(self):
        print(self.name.upper())
    def low(self):
        print(self.surname.lower())

user = Student()
user.show()
user.low()