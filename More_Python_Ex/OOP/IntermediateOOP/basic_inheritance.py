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

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# emp_1 = Employee('Manisha', 'Sinha', 60000)
# emp_2 = Employee('Amit', 'Mishra', 76000)

dev_1 = Developer('Manisha', 'Sinha', 60000, 'Java')
dev_2 = Developer('Amit', 'Mishra', 76000, 'Python')

# print(dev_1.fullname())
# print(dev_2.email)

print(dev_1.pay)
dev_1.emp_raise()
print(dev_1.pay)

