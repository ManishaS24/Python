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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.amount_raise = amount
    
    @classmethod
    def from_string(cls, emp_string):
         first, last, sal = emp_string.split('-')
         return cls(first, last, sal)


emp_1 = Employee('Manisha', 'Sinha', 60000)
emp_2 = Employee('Amit', 'Mishra', 76000)

Employee.set_raise_amount(1.07)
# emp_1.set_raise_amount(1.07)

print(emp_1.amount_raise)
print(emp_2.amount_raise)
print(Employee.amount_raise)

# new_emp_string = "John-Deo-12000"
# first, last, sal = new_emp_string.split('-')
# new_emp_1 = Employee(first, last, sal)
# print(new_emp_1.email)

print(Employee.from_string("John-Deo-12000").email)
