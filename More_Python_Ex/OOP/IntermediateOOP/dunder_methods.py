class Employee:
    amount_raise = 1.04

   
    def __init__(self, first_name, last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@' + 'company.com'
    

    def fullname(self):
        return '{} {} '.format(self.first_name, self.last_name)
    
    def emp_raise(self):
        self.pay = int(self.pay * self.amount_raise)
        # self.pay = int(self.pay * Employee.amount_raise)

    def __repr__(self): 
        return "Employee('{}', '{}', '{}')".format(self.first_name, self.last_name, self.pay)

    def __str__(self): 
        return "'{}'-'{}'".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
        
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Amit', 'Mishra', 76000)
emp_2 = Employee('Sumit', 'Mehra', 50000)

# print(emp_1)
# print(str(emp_1))

# print(repr(emp_1))
# print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1 + emp_2)

# print(len('test'))
# print('test'.__len__())

print(len(emp_1))