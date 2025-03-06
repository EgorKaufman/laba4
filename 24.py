class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = str(salary)
        
employees = [
    Employee('Egor', 1000),
    Employee('Artem', 999),
    Employee('Igor', 800)
]
    
for employee in employees:
    print(employee.name,employee.salary)