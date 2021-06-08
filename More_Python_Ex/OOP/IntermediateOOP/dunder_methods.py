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

emp_1 = Employee('Amit', 'Mishra', 76000)
print(emp_1)
