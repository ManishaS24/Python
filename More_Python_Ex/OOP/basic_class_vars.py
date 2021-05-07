class Employee:
    no_of_employees = 0
    amount_raise = 1.04


    def __init__(self, first_name, last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@' + 'company.com'
    
    no_of_employees += 1

    def fullname(self):
        return '{} {} '.format(self.first_name, self.last_name)
    
    def emp_raise(self):
        self.pay = int(self.pay * self.amount_raise)
        # self.pay = int(self.pay * Employee.amount_raise)

print(Employee.no_of_employees)

emp_1 = Employee('Manisha', 'Sinha', 60000)
emp_2 = Employee('Amit', 'Mishra', 76000)

print(Employee.no_of_employees)
""" 
print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__) """


print(emp_1.pay)
emp_1.emp_raise()
print(emp_1.pay)

Employee.amount_raise = 1.05

print(emp_1.amount_raise)
print(emp_2.amount_raise)
print(Employee.amount_raise)


emp_1.amount_raise = 1.06

""" print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__) """

print(emp_1.amount_raise)
print(emp_2.amount_raise)
print(Employee.amount_raise)

