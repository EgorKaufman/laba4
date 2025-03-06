class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class EmployeeCollection:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def show_employee(self):
        for employee in self.employees:
            print(f"Имя Фамилия: {employee.name}, Зарплата: {employee.salary}")
            
    def total_salary(self):
        return sum(employee.salary for employee in self.employees)
        
    def average_salary(self):
        if not self.employees:
            return 0
        return self.total_salary()/ len(self.employees)
        
collection = EmployeeCollection()
collection.add_employee(Employee("Егор Дойников", 50000))
collection.add_employee(Employee("Иван Романов", 5000))
collection.add_employee(Employee("Лев Белавин", 50001))

collection.show_employee()
print(f"Суммарная зарплата: {collection.total_salary()}")
print(f"Средняя зарплата: {collection.average_salary()}")               
            