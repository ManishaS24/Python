class Employee:
    def __init__(self, first_name, last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@' + 'company.com'

    def fullname(self):
        return '{} {} '.format(self.first_name, self.last_name)

"""emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2) """

""" emp_1.first_name = 'Manisha'
emp_1.last_name = 'Sinha'
emp_1.email = 'manisha.sinha@company.com'
emp_1.pay = 70000

emp_2.first_name = 'Ajay'
emp_2.last_name = 'Dogra'
emp_2.email = 'ajay.dogra@company.com'
emp_2.pay = 75000

print(emp_1.email, emp_2.email) """

emp_1 = Employee('Manisha', 'Sinha', 60000)
emp_2 = Employee('Amit', 'Mishra', 76000)

print(emp_1.email, emp_2.email)

print(emp_1.fullname(), emp_2.fullname())

